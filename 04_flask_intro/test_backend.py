import requests

BASE_URL = "http://localhost:5000"


def test_index(base_url=BASE_URL, endpoint="/"):
    _url = f"{base_url}{endpoint}"
    _r = requests.get(_url)
    _response = _r.json()
    _expected_response = {"greeting": "Hello, world!"}
    assert _response == _expected_response


def test_greet(base_url=BASE_URL, endpoint="/greeting"):
    test_index(base_url, endpoint)


def test_greet_user(base_url=BASE_URL, endpoint="/greeting"):
    _users = ["James", "Anna", "Beowulf", "Hildegard"]
    for _user in _users:
        _url = f"{base_url}{endpoint}/{_user}"
        _r = requests.get(_url)
        _response = _r.json()
        _expected_response = {"greeting": "Hello", "user": _user}
        assert _response == _expected_response

def test_add_by_api(base_url=BASE_URL, endpoint="/math/sum"):
    _url = f"{base_url}{endpoint}"
    _body = {"add": [1, 2, 3, 4, 5]}
    _r = requests.post(_url, data=_body)
    _response = _r.json()
    _expected_response = {"sum": 15.0}
    assert _response == _expected_response