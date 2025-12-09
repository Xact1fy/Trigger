import os
import argparse
import subprocess
import socket
import platform

# 1. Pending Create a good banner ✅
# 2. Learn how this shit works

def banner():
    print("""
 ██▀███   ██▓  ▄████   ▄████ ▓█████  ██▀███  
▓██ ▒ ██▒▓██▒ ██▒ ▀█▒ ██▒ ▀█▒▓█   ▀ ▓██ ▒ ██▒
▓██ ░▄█ ▒▒██▒▒██░▄▄▄░▒██░▄▄▄░▒███   ▓██ ░▄█ ▒
▒██▀▀█▄  ░██░░▓█  ██▓░▓█  ██▓▒▓█  ▄ ▒██▀▀█▄  
░██▓ ▒██▒░██░░▒▓███▀▒░▒▓███▀▒░▒████▒░██▓ ▒██▒
░ ▒▓ ░▒▓░░▓   ░▒   ▒  ░▒   ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░▒ ░ ▒░ ▒ ░  ░   ░   ░   ░  ░ ░  ░  ░▒ ░ ▒░
  ░░   ░  ▒ ░░ ░   ░ ░ ░   ░    ░     ░░   ░ 
   ░      ░        ░       ░    ░  ░   ░     
                                             
          """)

def create_cli_parser():
    """
    Creates and returns the CLI argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Host Discovery and Status Checker Tool",
        epilog="Example: python3 main.py -t example.com"
    )
    parser.add_argument(
        '-t', '--target',
        required=True,
        help='Target hostname or IP address to discover and check status.'
    )
    parser.add_argument(
        '-l', '--online',
        action='store_true',
        help='checks if the target is active or sleeping with a ping scan.'
    )
    parser.add_argument(
        '-n' '--hostname',
        action='store_true',
        help='Ping for hostname.'
    )
    parser.add_argument(
        '-i' '--ipaddress',
        action='store_true',
        help='Ping for IP address.'
    )
    parser.add_argument(
        '-r' '--telnet',
        action='store_true',
        help='Try a telnet connection.'
    )
    parser.add_argument(
        '-p' '--port',
        type=int,
        default=80,
        help='Port number for telnet connection.'
    )
    return parser

def active(target):
    """
    Pings the target to check if it is active.
    Returns True if active, False otherwise.
    """
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', target]
    
    try:
        subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
        print(f"🔄 {target} is active.")
    except subprocess.CalledProcessError:
        print(f"🛑 {target} is inactive.")

def namefinder(target):
    """
    Resolves the hostname for the given IP address.
    """
    try:
        hostname = socket.gethostbyaddr(target)
        print(f"🔄 Hostname for {target} is {hostname}.")
    except socket.herror:
        print(f"🛑 Could not resolve hostname for {target}.")

def ipfinder(target):
    """
    Resolves the IP address for the given hostname.
    """
    try:
        ip_address = socket.gethostbyname(target)
        print(f"🔄 IP address for {target} is {ip_address}.")
    except socket.gaierror:
        print(f"🛑 Could not resolve IP address for {target}.")

def telnet_connect(target, port):
    """
    Attempts to establish a telnet connection to the target on the specified port.
    """
    try:
        with socket.create_connection((target, port), timeout=5):
            print(f"🔄 Successfully connected to {target} on port {port}.")
    except (socket.timeout, ConnectionRefusedError, OSError):
        print(f"🛑 Could not connect to {target} on port {port}.")

def cli_host_discoverer(target):
    """
    Main function to handle CLI host discovery and status checking.
    """
    parser = create_cli_parser()
    args = parser.parse_args()

    if args.online:
        active(target)
    if args.n__hostname:
        namefinder(target)
    if args.i__ipaddress:
        ipfinder(target)
    if args.r__telnet:
        telnet_connect(target, args.port)

if __name__ == "__main__":
    banner()
    parser = create_cli_parser()
    args = parser.parse_args()
    cli_host_discoverer(args.target)

