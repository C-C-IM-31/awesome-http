METHODS = (
    "GET",
    "POST",
    "PUT",
    "DELETE",
    "OPTIONS",
    "HEAD",
    "TRACE",
    "CONNECT",
)

def parse_request_line(line: str) -> tuple[str, str, str] | None:
    parsed = line.strip().split(" ")
    valid = len(parsed) == 3 and parsed[0] in METHODS and parsed[2].startswith("HTTP")
    return parsed if valid else None
