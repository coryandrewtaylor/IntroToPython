def test_index(client):
    r = client.get("/")
    assert r.status_code == 200
    assert b"This is a tutorial Flask application" in r.data


def test_greet(client):
    r = client.get("/greeting")
    assert r.status_code == 200
    assert b"Hello, world!" in r.data


def test_greet_user(client, test_strings):
    for s in test_strings:
        _route = f"/greeting/{s}"
        r = client.get(_route)

        assert r.status_code == 200
        assert f"Hello, {s}!".encode() in r.data
