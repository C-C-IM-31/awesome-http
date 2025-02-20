import asyncio
from http_server import HTTPServer
from handler import HTTPHandler
import json
from datetime import datetime, timezone

host = "127.0.0.1"
port = 8000

async def get_time():
    time = datetime.now(timezone.utc).isoformat()
    return json.dumps({"time": time})

async def main():
    http_handler = HTTPHandler()
    http_handler.add_route("GET", "/time", get_time)
    http_server = HTTPServer(host, port, http_handler)
    await http_server.serve_forever()


if __name__ == "__main__":
    server = asyncio.get_event_loop().run_until_complete(main())
    asyncio.run(main())
