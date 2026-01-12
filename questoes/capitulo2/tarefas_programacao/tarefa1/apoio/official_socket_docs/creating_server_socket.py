"""
Here I'm following the tutorial of the socket python library.
URL: https://docs.python.org/pt-br/3.9/howto/sockets.html
"""

import socket

MAX_CONNECTIONS = 5

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 80))
serversocket.listen(MAX_CONNECTIONS)

# while True:
#     # accept connections from outside
#     (clientsocket, adress) = serversocket.accept()
    
#     # do something with clientsocket 
#     print('doing something...')


    