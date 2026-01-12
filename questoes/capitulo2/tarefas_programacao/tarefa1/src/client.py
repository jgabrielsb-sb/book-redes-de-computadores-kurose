from utils import LOCALHOST, PORT, HTTPRequest, MethodEnum, format_http_request

import socket

# preparing socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((LOCALHOST, PORT))

resource_to_get = "/home/jgabrielsb/Documents/Programming/Estudos/redes_computadores_kurose/questoes/capitulo2/tarefas_programacao/tarefa1/src/html_file.html"

http_request = HTTPRequest(
    method=MethodEnum.POST,
    host=f"{LOCALHOST}:{PORT}",
    resource=resource_to_get
)
http_request_as_str = format_http_request(http_request)

client.sendall(http_request_as_str.encode())

response = client.recv(2048)
print(response)

