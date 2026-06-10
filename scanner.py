import socket
import sys
from datetime import datetime

print("-" * 50)
print("   🔒 Custom Network Port Scanner 🔒   ")
print("-" * 50)

# 1. Get dynamic input from the user
target_input = input("Enter target host/IP (e.g., localhost or 8.8.8.8): ")
if not target_input.strip():
    print("Target cannot be empty. Exiting.")
    sys.exit()

try:
    # Resolve target to IP address
    target_ip = socket.gethostbyname(target_input)
except socket.gaierror:
    print(f"\n[!] Error: Hostname '{target_input}' could not be resolved.")
    sys.exit()

try:
    start_port = int(input("Enter starting port (e.g., 1): "))
    end_port = int(input("Enter ending port (e.g., 100): "))
    if start_port < 1 or end_port > 65535 or start_port > end_port:
        print("[!] Invalid port range. Ports must be between 1 and 65535.")
        sys.exit()
except ValueError:
    print("[!] Please enter valid integers for port numbers.")
    sys.exit()

print("-" * 50)
print(f"Scanning Target : {target_ip} ({target_input})")
print(f"Scanning Ports  : {start_port} through {end_port}")
print(f"Time Started    : {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
print("-" * 50)

open_ports = []

# 2. Run the scanning loop across the specified range
try:
    for port in range(start_port, end_port + 1):
        # Quick visual feedback in the terminal line
        print(f"Scanning port {port}...", end="\r", flush=True)
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Shorter timeout speeds up the scan
        
        result = s.connect_ex((target_ip, port))
        if result == 0:
            print(f"🟢 Port {port}: OPEN       ")  # Extra spaces clear out old characters
            open_ports.append(port)
        s.close()

    print("\n" + "-" * 50)
    print("   Scan Complete!   ")
    print("-" * 50)
    if open_ports:
        print(f"Summary of open ports: {', '.join(map(str, open_ports))}")
    else:
        print("No open ports found in that range.")

except KeyboardInterrupt:
    print("\n\n[!] Scan stopped by user. Exiting...")
    sys.exit()
except socket.error:
    print("\n[!] Network error encountered. Connection lost.")
    sys.exit()