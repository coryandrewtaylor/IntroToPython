import pytest
from flask import Flask

from flask_intro.backend import configure_routes

@pytest.fixture
def app():
    _app = Flask("testing")
    configure_routes(_app)
    _app.testing = True
    return _app


@pytest.fixture
def client(app):
    return app.test_client()
