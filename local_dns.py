import socket

hostname = socket.gethostname()
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try:
    sock.connect(("8.8.8.8", 80))
    local_ip = sock.getsockname()[0]
finally:
    sock.close()

print("Host Name :", hostname)
print("IP Address:", local_ip)

# Show DNS resolver addresses when available (Linux)
try:
    with open("/etc/resolv.conf", encoding="utf-8") as file:
        servers = [line.split()[1] for line in file if line.startswith("nameserver")]
    print("DNS Server(s):", ", ".join(servers) if servers else "Not listed")
except OSError:
    print("DNS Server(s): Check your operating system network settings")
