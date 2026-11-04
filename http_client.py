import socket

HOST = "127.0.0.1"
PORT = 8080
request = ("GET / HTTP/1.1\r\n"
           f"Host: {HOST}\r\n"
           "Connection: close\r\n\r\n")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(request.encode())
    response = bytearray()
    while True:
        chunk = client.recv(4096)
        if not chunk:
            break
        response.extend(chunk)

print(response.decode(errors="replace"))
