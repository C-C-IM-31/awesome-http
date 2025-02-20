import asyncio
from http_server import HTTPServer

host = "127.0.0.1"
port = 8000

async def main():
    http_server = HTTPServer(host, port)
    await http_server.serve_forever()


if __name__ == "__main__":
    server = asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())
