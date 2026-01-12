import socket

LOCALHOST = '127.0.0.1'
PORT = 65432
MAX_CONNECTIONS = 5

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(MAX_CONNECTIONS)

while True:
    client, addr = server.accept()

    message = client.recv(1024)
    
    client.send(f"Hello client {addr}".encode())