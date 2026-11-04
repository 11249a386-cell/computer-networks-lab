import socket

HOST, PORT = "127.0.0.1", 65432
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"Echo server listening on {PORT}")
    conn, address = server.accept()
    with conn:
        print("Connected:", address)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print("Received:", data.decode(errors="replace"))
            conn.sendall(data)
