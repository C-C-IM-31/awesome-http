import asyncio
from typing import Callable

from handler import HTTPhandler


class HTTPServer:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._handler = HTTPhandler()

    def add_route(self) -> Callable:
        return self._handler.add_route

    async def serve_forever(self):
        server = await asyncio.start_server(self._handler.handler, self._host, self._port)
        async with server:
            await server.serve_forever()