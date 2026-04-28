from urllib.parse import urlparse


def is_success_status(status_code: int) -> bool:
    return 200 <= status_code < 300


def is_valid_url(url: str) -> bool:
    parsed = urlparse(url)
    return bool(parsed.scheme in {"http", "https"} and parsed.netloc)
