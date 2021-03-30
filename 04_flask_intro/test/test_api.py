def test_greet_user(client, test_strings):
    for s in test_strings:
        _route = f"/api/v1/greeting/{s}"
        r = client.get(_route)
        assert r.status_code == 200
        assert r.json == {"greeting": "Hello", "user": s}


def test_add_int_success(client, test_ints):
    _data = {"add": test_ints}
    r = client.post("/api/v1/math/sum", data=_data)
    assert r.status_code == 200
    assert r.json == {"sum": float(sum(test_ints))}


def test_add_float_success(client, test_floats):
    _data = {"add": test_floats}
    r = client.post("/api/v1/math/sum", data=_data)
    assert r.status_code == 200
    assert r.json == {"sum": sum(test_floats)}


def test_add_bad_key_failure(client, test_ints):
    _data = {"junk": test_ints}
    r = client.post("/api/v1/math/sum", data=_data)
    assert r.status_code == 400


def test_add_bad_data_failure(client, test_strings):
    _data = {"add": test_strings}
    r = client.post("/api/v1/math/sum", data=_data)
    assert r.status_code == 400