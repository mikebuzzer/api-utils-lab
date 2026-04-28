import time


def current_timestamp_ms() -> int:
    return int(time.time() * 1000)

def response_time_ms(start_ms: int, end_ms: int) -> int:
    return end_ms - start_ms
