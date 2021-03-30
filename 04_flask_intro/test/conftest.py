import os.path

import pytest

from flask_intro import create_app

@pytest.fixture
def app():
    _secret_key_path = os.path.abspath("./SECRET_KEY.txt")
    _app = create_app(_secret_key_path)
    _app.testing = True
    return _app


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def test_strings():
    return ["a", "b", "c", "d", "e"]


@pytest.fixture
def test_ints():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def test_floats():
    return [1.0, 2.0, 3.0, 4.0, 5.0]