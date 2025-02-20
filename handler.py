from asyncio import StreamReader, StreamWriter
from typing import Callable
import json

class HTTPHandler:

    ROUTES = {
        "GET": {},
        "POST": {},
        "PUT": {},
        "DELETE": {},
        "OPTIONS": {},
        "HEAD": {},
        "TRACE": {},
        "CONNECT": {}
    }

    def add_route(self, method: str, path: str, handler: Callable) -> None:
        self.ROUTES[method][path] = handler

    async def handler(self, reader: StreamReader, writer: StreamWriter):
        request = await reader.read(1024)
        request_line = request.decode().split("\r\n")[0]
        print(self._parse_request_line(request_line)) # can be deleted later
        parsed_line = self._parse_request_line(request_line)

        response_status = "400 Bad Request"
        response = json.dumps({})

        if parsed_line:
            method, path = parsed_line[0], parsed_line[1]
            if self.ROUTES.get(method).get(path):
                response_status = "200 OK"
                response = await self.ROUTES.get(method).get(path)()
            else:
                response_status = "404 Not Found"

        http_header = self._get_header(response_status, response)
        packet = http_header + response
        writer.write(packet.encode())
        await writer.drain()
        writer.close()
        await writer.wait_closed()

    def _parse_request_line(self, line: str) -> tuple[str, str, str] | None:
        parsed = line.strip().split(" ")
        valid = len(parsed) == 3 and parsed[0] in self.ROUTES.keys() and parsed[2].startswith("HTTP")
        return parsed if valid else None

    @staticmethod
    def _get_header(response_status: str, response: str) -> str:
        return (
            f"HTTP/1.1 {response_status}\r\n"
            "Content-Type: text/plain\r\n"
            f"Content-Length: {len(response)}\r\n"
            "\r\n"
        )