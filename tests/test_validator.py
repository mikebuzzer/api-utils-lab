from api_utils.validator import is_success_status, is_valid_url


def test_is_success_status_200():
    assert is_success_status(200) is True


def test_is_success_status_201():
    assert is_success_status(201) is True


def test_is_success_status_204():
    assert is_success_status(204) is True


def test_is_success_status_299():
    assert is_success_status(299) is True


def test_is_success_status_300():
    assert is_success_status(300) is False


def test_is_success_status_400():
    assert is_success_status(400) is False


def test_is_success_status_500():
    assert is_success_status(500) is False


def test_is_valid_url_https():
    assert is_valid_url("https://example.com") is True


def test_is_valid_url_http():
    assert is_valid_url("http://example.com") is True


def test_is_valid_url_with_path():
    assert is_valid_url("https://example.com/api/data") is True


def test_is_valid_url_with_query_params():
    assert is_valid_url("https://example.com/search?q=test") is True


def test_is_valid_url_without_scheme():
    assert is_valid_url("example.com") is False


def test_is_valid_url_random_text():
    assert is_valid_url("not-a-url") is False


def test_is_valid_url_empty_string():
    assert is_valid_url("") is False


def test_is_valid_url_ftp_scheme():
    assert is_valid_url("ftp://example.com") is False
