import time


def current_timestamp_ms() -> int:
    return int(time.time() * 1000)
