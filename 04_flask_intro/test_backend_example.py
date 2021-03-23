import requests

BASE_URL = "http://localhost:5000"


def test_index(base_url: str = BASE_URL, endpoint: str = "/") -> None:
    _url = f"{base_url}{endpoint}"
    _r = requests.get(_url)
    _response = _r.json()
    _expected_response = {"greeting": "Hello, world!"}
    assert _response == _expected_response


def test_greet(base_url: str = BASE_URL, endpoint: str = "/greeting") -> None:
    test_index(base_url=base_url, endpoint=endpoint)


def test_greet_user(base_url: str = BASE_URL, endpoint: str = "/greeting") -> None:
    _users = ["James", "Anna", "Beowulf", "Hildegard"]
    for _user in _users:
        _url = f"{base_url}{endpoint}/{_user}"
        _r = requests.get(_url)
        _response = _r.json()
        _expected_response = {"greeting": "Hello", "user": _user}
        assert _response == _expected_response
