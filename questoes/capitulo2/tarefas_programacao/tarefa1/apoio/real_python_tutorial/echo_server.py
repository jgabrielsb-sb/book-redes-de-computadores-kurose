import socket
import time

# 1 - server sets up a listening socket

HOST = '127.0.0.1'
PORT = 65432

def get_all_bytes(s: socket.socket, chunk_size: int = 8) -> bytes:
    """
    This function is for learning purposes.
    The main intention here is to get all bytes of the buffer given a socket
    connection and a chunk size.

    :param socket: the socket connection
    :type socket: socket.Socket()
    :param chunk_size: the chunk size in bytes
    :type chunk_size: int
    :return: all bytes present on the buffer
    :rtype: bytes
    """
    chunks = []

    while True:
        print('calling recv')
        chunk = s.recv(chunk_size)
        print(f'chunk: {chunk}')

        if not chunk:
            print('break')
            break

        chunks.append(chunk)

    print('saiu do loop')
    return b''.join(chunks)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # dont need s.close()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept() # conn - new socket object used to send/receive data on this connection. add- internet adress of the client

    with conn:
        print(f"Connected by {addr}")

        while True:
            data = get_all_bytes(conn)
            
            # if not data:
            #     break

            # how_many_bytes_send = conn.send(data)
            # print(how_many_bytes_send)
            

        
