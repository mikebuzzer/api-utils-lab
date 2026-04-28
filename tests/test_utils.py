from api_utils.utils import current_timestamp_ms


def test_current_timestamp_ms_returns_int():
    assert isinstance(current_timestamp_ms(), int)
