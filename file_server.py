import socket
import struct

HOST, PORT = "127.0.0.1", 12345
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen(1)
    print(f"File server listening on {PORT}")
    conn, address = server.accept()
    with conn:
        print("Connected:", address)
        name_len = struct.unpack("!H", conn.recv(2))[0]
        filename = conn.recv(name_len).decode()
        safe_name = filename.replace("/", "_").replace("\\\\", "_")
        size = struct.unpack("!Q", conn.recv(8))[0]
        received = 0
        output_name = "received_" + safe_name
        with open(output_name, "wb") as output:
            while received < size:
                chunk = conn.recv(min(4096, size - received))
                if not chunk:
                    raise ConnectionError("Connection ended before file was complete")
                output.write(chunk)
                received += len(chunk)
        print(f"File saved as {output_name} ({received} bytes)")
