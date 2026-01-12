
import socket
import os
import base64

from pydantic import ValidationError
from utils import LOCALHOST, PORT, HTTPRequest, parse_http_request, MethodEnum, HTTPResponse, format_http_response
from pathlib import Path



def get_file_as_base64_str(file_path: Path) -> str:
    if not isinstance(file_path, Path):
        raise TypeError("file_path must be of type Path")
    if not file_path.exists():
        raise FileNotFoundError(f"file not found: {file_path}")

    data = file_path.read_bytes() 
    return base64.b64encode(data).decode("ascii")

def process_http_request(http_request: HTTPRequest) -> HTTPResponse:
    try:
        http_request = parse_http_request(http_request_as_str)

        if http_request.method != MethodEnum.GET:
           return HTTPResponse(
                status_code=405,
                message=f"The method {http_request.method.value} is not allowed",
                content_length=0,
                content=b''
            )
        
        try:
            file_path = Path(http_request.resource)
            file_content = get_file_as_base64_str(file_path)
            return HTTPResponse(
                status_code=200,
                message="OK",
                content_length=len(file_content),
                content=file_content.encode()
            )

        except Exception as e:
            return HTTPResponse(
                status_code=404,
                message=f"Error getting the resouce {http_request.resource}: {e}",
                content_length=0,
                content=b''
            )
        
    except ValidationError:
        return HTTPResponse(
            status_code=400,
            message="Bad Request",
            content_length=0,
            content=b''
        )

    
MAX_CONNECTIONS = 5

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
server.listen(MAX_CONNECTIONS)

message_to_send_back = ""

while True:
    client, addr = server.accept()
    
    http_request_as_str = client.recv(1024).decode()
    http_response = process_http_request(http_request_as_str)
    http_response_as_str = format_http_response(http_response)
    client.sendall(http_response_as_str.encode())