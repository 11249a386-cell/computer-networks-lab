import socket
import threading

HOST, PORT = "127.0.0.1", 55555

def receive_messages(sock):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("Server disconnected.")
                break
            print("\\n" + data.decode(errors="replace"))
        except OSError:
            break

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print("Connected. Open another client to chat. Type exit to quit.")
    threading.Thread(target=receive_messages, args=(client,), daemon=True).start()
    while True:
        message = input()
        if message.lower() == "exit":
            break
        client.sendall(message.encode())
