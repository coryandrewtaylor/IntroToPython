some_ints = [1, 2, 3, 4]
some_strs = ["a", "b", "c"]


def test_index(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.json == {"greeting": "Hello, world!"}


def test_greet(client):
    r = client.get("/greeting")
    assert r.status_code == 200
    assert b"Hello, world!" in r.data


def test_greet_user(client):
    for _user in some_strs:
        _route = f"/greeting/{_user}"
        r = client.get(_route)
        _data = f"Hello, {_user}!".encode()

        assert r.status_code == 200
        assert _data in r.data


def test_api_greet_user(client):
    for _user in some_strs:
        _route = f"api/v1/greeting/{_user}"
        r = client.get(_route)
        assert r.status_code == 200
        assert r.json == {"greeting": "Hello", "user": _user}


def test_add_by_api(client):
    _data = {"add": some_ints}
    r = client.post("api/v1/math/sum", data=_data)
    assert r.status_code == 200
    assert r.json == {"sum": float(sum(some_ints))}


def test_add_by_api_bad_key(client):
    _data = {"junk": some_ints}
    r = client.post("api/v1/math/sum", data=_data)
    assert r.status_code == 400


def test_add_by_api_bad_data(client):
    _data = {"add": some_strs}
    r = client.post("api/v1/math/sum", data=_data)
    assert r.status_code == 400