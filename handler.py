from asyncio import StreamReader, StreamWriter
import json
from datetime import datetime, timezone
from parsers import parse_request_line

async def handler(reader: StreamReader, writer: StreamWriter):
    request = await reader.read(1024)
    request_line = request.decode().split("\r\n")[0]
    print(parse_request_line(request_line))
    time = datetime.now(timezone.utc).isoformat()
    response = json.dumps({"time": time})
    http_header = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response)}\r\n"
        "\r\n"
    )
    packet = http_header + response
    writer.write(packet.encode())
    await writer.drain()
    writer.close()
    await writer.wait_closed()
