from api_utils.utils import current_timestamp_ms, response_time_ms


def test_current_timestamp_ms_returns_int():
    result = current_timestamp_ms()
    assert isinstance(result, int)


def test_current_timestamp_ms_positive():
    result = current_timestamp_ms()
    assert result > 0


def test_response_time_ms_basic():
    assert response_time_ms(1000, 1250) == 250


def test_response_time_ms_zero_difference():
    assert response_time_ms(1000, 1000) == 0


def test_response_time_ms_negative_difference():
    assert response_time_ms(1250, 1000) == -250
