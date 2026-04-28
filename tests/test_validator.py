from api_utils.validator import is_success_status, is_valid_url


def test_is_success_status_true():
    assert is_success_status(200) is True


def test_is_success_status_false():
    assert is_success_status(404) is False


def test_is_valid_url_true():
    assert is_valid_url("https://example.com") is True


def test_is_valid_url_false():
    assert is_valid_url("not-a-url") is False
