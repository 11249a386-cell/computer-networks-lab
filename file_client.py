import socket
import struct
from pathlib import Path

HOST, PORT = "127.0.0.1", 12345
path = Path(input("Enter file path to send: ")).expanduser()
if not path.is_file():
    raise SystemExit("File not found")
name = path.name.encode()
size = path.stat().st_size
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(struct.pack("!H", len(name)) + name + struct.pack("!Q", size))
    with path.open("rb") as source:
        while chunk := source.read(4096):
            client.sendall(chunk)
print("File sent successfully")
