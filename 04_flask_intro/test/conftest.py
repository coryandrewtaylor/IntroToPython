import pytest

from flask_intro import create_app

@pytest.fixture
def app():
    _app = create_app()
    _app.testing = True
    return _app


@pytest.fixture
def client(app):
    return app.test_client()
