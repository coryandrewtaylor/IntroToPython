import os.path

import pytest

from flask_intro import create_app

@pytest.fixture
def app():
    _secret_key_path = os.path.abspath("../SECRET_KEY.txt")
    _app = create_app(_secret_key_path)
    _app.testing = True
    return _app


@pytest.fixture
def client(app):
    return app.test_client()
