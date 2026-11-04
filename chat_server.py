import socket
import threading

HOST, PORT = "127.0.0.1", 55555
clients = set()
lock = threading.Lock()

def handle_client(conn, address):
    print("Connected:", address)
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode(errors="replace")
            print(f"{address}: {message}")
            with lock:
                recipients = list(clients)
            for client in recipients:
                if client is not conn:
                    try:
                        client.sendall(f"{address}: {message}".encode())
                    except OSError:
                        pass
    finally:
        with lock:
            clients.discard(conn)
        conn.close()
        print("Disconnected:", address)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Chat server listening on {PORT}")
    while True:
        conn, address = server.accept()
        with lock:
            clients.add(conn)
        threading.Thread(target=handle_client, args=(conn, address), daemon=True).start()
