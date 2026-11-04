arp_table = {
    "192.168.1.1": "00:0a:95:9d:68:16",
    "192.168.1.2": "00:0a:95:9d:68:17",
    "192.168.1.3": "00:0a:95:9d:68:18",
}
rarp_table = {mac: ip for ip, mac in arp_table.items()}

while True:
    print("\\n1. ARP (IP to MAC)\\n2. RARP (MAC to IP)\\n3. Exit")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        ip = input("Enter IP address: ").strip()
        mac = arp_table.get(ip)
        print(f"ARP Reply: {ip} is at {mac}" if mac else "IP address not found")
    elif choice == "2":
        mac = input("Enter MAC address: ").strip().lower()
        result = rarp_table.get(mac)
        print(f"RARP Reply: {mac} is associated with IP {result}" if result else "MAC address not found")
    elif choice == "3":
        break
    else:
        print("Invalid choice")
