import socket

HOST = "127.0.0.1"
PORT = 8080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"HTTP server running at http://{HOST}:{PORT}")
    while True:
        conn, address = server.accept()
        with conn:
            request = conn.recv(4096).decode(errors="replace")
            print("Request received from", address)
            body = "<html><body><h1>Welcome to Computer Networks Lab!</h1></body></html>"
            response = ("HTTP/1.1 200 OK\r\n"
                        "Content-Type: text/html; charset=utf-8\r\n"
                        f"Content-Length: {len(body.encode())}\r\n"
                        "Connection: close\r\n\r\n" + body)
            conn.sendall(response.encode())
