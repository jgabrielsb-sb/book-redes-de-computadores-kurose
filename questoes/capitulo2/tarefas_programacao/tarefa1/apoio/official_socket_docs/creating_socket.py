#https://docs.python.org/pt-br/3.9/howto/sockets.html

"""
Here I'm following the tutorial of the socket python library.
URL: https://docs.python.org/pt-br/3.9/howto/sockets.html
"""
import socket

## CREATING A SOCKET ##
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
s.connect(("www.python.org", 80))


