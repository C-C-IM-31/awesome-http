import asyncio
from handler import HTTPHandler


class HTTPServer:
    def __init__(self, host: str, port: int, handler: HTTPHandler=HTTPHandler()):
        self._host = host
        self._port = port
        self._handler = handler

    async def serve_forever(self):
        server = await asyncio.start_server(self._handler.handler, self._host, self._port)
        async with server:
            await server.serve_forever()