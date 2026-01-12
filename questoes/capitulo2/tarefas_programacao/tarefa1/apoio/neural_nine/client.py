import socket

LOCALHOST= '127.0.0.1'
PORT_TO_CONNECT_TO = 65432

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LOCALHOST, PORT_TO_CONNECT_TO))
client.send(b'Hello from client')

message_received = client.recv(1024)
print(message_received.decode())