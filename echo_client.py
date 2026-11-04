import socket

HOST, PORT = "127.0.0.1", 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    while True:
        message = input("Enter message (exit to stop): ")
        client.sendall(message.encode())
        reply = client.recv(1024)
        if not reply:
            break
        print("Echo from server:", reply.decode(errors="replace"))
        if message.lower() == "exit":
            break
