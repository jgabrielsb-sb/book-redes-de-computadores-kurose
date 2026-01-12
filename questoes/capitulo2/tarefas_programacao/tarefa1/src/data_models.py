from pydantic import BaseModel, ConfigDict
from enum import Enum

LOCALHOST = '127.0.0.1'
PORT = 65432

class MethodEnum(Enum):
    POST = "POST"
    GET = "GET"
    UPDATE = "UPDATE"
    DELETE = "DELETE"

class HTTPRequest(BaseModel):
    method: MethodEnum
    host: str
    resource: str

    model_config = ConfigDict(arbitrary_types_allowed=True)

class HTTPResponse(BaseModel):
    status_code: int
    message: str
    content_length: int
    content: bytes

    model_config = ConfigDict(arbitrary_types_allowed=True)

def format_http_request(http_request: HTTPRequest) -> str:
    """
    Formats the HTTP request as a string and returns the string.
    :param http_request: The HTTP request object to format.
    :return: The formatted string.
    :raises TypeError: If the HTTP request object is not of type HTTPRequest.
    """
    if not isinstance(http_request, HTTPRequest):
        raise TypeError('http_request must be of type HTTPRequest')

    method = http_request.method.value
    resource = http_request.resource
    host = http_request.host

    http_request_as_str = f"""{method} {resource} HTTP/1.0\nHost: {host}\r\n\r\n"""

    return http_request_as_str

def parse_http_request(http_request_as_str: str) -> HTTPRequest:
    """
    Parses the HTTP request as a string and returns the HTTP request object.
    :param http_request_as_str: The HTTP request as a string to parse.
    :return: The HTTP request object.
    :raises TypeError: If the HTTP request as a string is not of type str.
    """
    if not isinstance(http_request_as_str, str):
        raise TypeError('http_request_as_str must be of type str')

    http_request_as_str = http_request_as_str.replace('\r', '')
    
    lines = http_request_as_str.split('\n')
    method = lines[0].split(' ')[0]
    resource = lines[0].split(' ')[1]
    host = lines[1].split(' ')[1]
    
    return HTTPRequest(method=method, resource=resource, host=host)

def format_http_response(http_response: HTTPResponse) -> str:
    """
    Formats the HTTP response as a string and returns the string.
    :param http_response: The HTTP response object to format.
    :return: The formatted string.
    :raises TypeError: If the HTTP response object is not of type HTTPResponse.
    """
    if not isinstance(http_response, HTTPResponse):
        raise TypeError('http_response must be of type HTTPResponse')
        
    return f"HTTP/1.0 {http_response.status_code} {http_response.message}\r\nContent-Length: {http_response.content_length}\r\n\r\n{http_response.content}"

def parse_http_response(http_response_as_str: str) -> HTTPResponse:
    """
    Parses the HTTP response as a string and returns the HTTP response object.
    :param http_response_as_str: The HTTP response as a string to parse.
    :return: The HTTP response object.
    :raises TypeError: If the HTTP response as a string is not of type str.
    """
    if not isinstance(http_response_as_str, str):
        raise TypeError('http_response_as_str must be of type str')

    lines = http_response_as_str.split('\n')
    status_code = lines[0].split(' ')[1]
    content_length = lines[1].split(' ')[1]
    content = lines[2]
    
    return HTTPResponse(status_code=status_code, content_length=content_length, content=content)

if __name__ == "__main__":
    http_request_as_str = """GET www.google.com/image HTTP/1.0\nHost: 127.0.0.1:65432\r\n\r\n"""
    http_request = parse_http_request(http_request_as_str)
    print(http_request)





