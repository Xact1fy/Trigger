![Hey. Nice to meet you... ](https://cdn.vectorstock.com/i/500p/84/91/pixel-night-sky-background-vector-59028491.jpg)


# 💥 Trigger: The Essential Network Quick-Check CLI

## 🚀 Overview

**Trigger** is a powerful, lightweight **Command Line Interface (CLI) utility** built in Python, designed for rapid network diagnosis and connectivity testing. It consolidates crucial troubleshooting steps—DNS resolution and port connectivity checks—into a single, easy-to-use tool. Ideal for network engineers and developers who need to quickly verify connectivity to services and resolve hostnames.

### Key Features:

* **⚡ Bidirectional Resolution:** Instantly look up the **IP address** for a given hostname, and vice versa.
* **🔌 Telnet Connectivity Tester:** Quickly attempt a **TCP connection** (Telnet) to a specific host and port to verify service reachability (e.g., checking if a web server's port 80 is open).

---

## 💻 Installation

Follow these steps to get **Trigger** ready to use on your system.

### Prerequisites

* **Python 3.x**
* No external Python libraries are required (standard libraries like `socket` are used).

### Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Xact1fy/Trigger.git](https://github.com/Xact1fy/Trigger.git)
    cd Trigger
    ```
2.  **Ensure the script is executable (optional, depending on your system):**
    ```bash
    chmod +x CLITOOL.py
    ```

---

## 🛠️ Usage

**Trigger** is executed directly using the Python 3 interpreter, followed by the script name and the required flags.

### Command Syntax

The core command structure is:

```bash
python3 CLITOOL.py -t <TARGET> [-i|-n|-r] [-p <PORT>]
```

| flag | description | Mandatory / Optional |
| :--- | :--- | :--- |
| -t | Enter the hostname or IP of the target | **Mandatory** |
| -i | **IP Address Lookup:** Resolves the target hostname to an IP address. | Optional |
| -n | **Hostname Lookup:** Resolves the target IP address to a hostname. | Optional |
| -r | **Telnet/Reachability Check:** Attempts a TCP connection to the specified target and port. | Optional |
| -p | Port: Specifies the port number to use with the ``` -r ``` flag (e.g., 80, 443, 22). | Required for -r |

## 👩‍💻 EXAMPLES 

### 1. Resolve Hostname to IP Address
```bash
Finds the IP address of example.com
python3 CLITOOL.py -t example.com -i
```
### 2. Resolve IP Address to Hostname
```bash
Finds the hostname associated with the IP 8.8.8.8
python3 CLITOOL.py -t 8.8.8.8 -n
```

### 3. Test HTTP Connectivity (Port 80)
```bash
Checks if example.com is reachable on standard HTTP port 80
python3 CLITOOL.py -t example.com -r -p 80
```

### 4. Test SSH Connectivity (Port 22)
```bash
Checks if a server is reachable for SSH connection
python3 CLITOOL.py -t 192.168.1.1 -r -p 22
```

## 📱 CONTACT 
**This has all my contacts: **https://github.com/Xact1fy/Xact1fy
