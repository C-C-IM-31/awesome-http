import asyncio
from handler import handler


class HTTPServer:
    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port


    async def serve_forever(self):
        server = await asyncio.start_server(handler, self._host, self._port)
        async with server:
            await server.serve_forever()