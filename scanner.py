import socket
import sys
from datetime import datetime

# Define the target (localhost means your own machine for safe testing)
TARGET = "localhost"

print("-" * 50)
print(f"Scanning Target: {TARGET}")
print(f"Time Started: {str(datetime.now())}")
print("-" * 50)

# We will scan a standard range of ports (e.g., common web/system ports)
ports_to_scan = [21, 22, 80, 443, 8080]

try:
    for port in ports_to_scan:
        # AF_INET specifies IPv4, SOCK_STREAM specifies TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so the script doesn't hang forever on a closed port
        s.settimeout(1.0)
        
        # connect_ex returns an error indicator (0 means connection succeeded)
        result = s.connect_ex((TARGET, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: Closed")
            
        # Always close the socket connection
        s.close()

except KeyboardInterrupt:
    print("\nExiting script...")
    sys.exit()

except socket.gaierror:
    print("\nHostname could not be resolved.")
    sys.exit()

except socket.error:
    print("\nCould not connect to server.")
    sys.exit()