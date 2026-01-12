import socket

# 2 - Client initiates a connection

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

# 3 - Data is exchanged

    s.sendall(b"Hello World")
    print('travado@')
    data = s.recv(1024)
    print(data)

print(f"Received: {data}")