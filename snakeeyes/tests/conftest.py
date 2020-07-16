import pytest

from snakeeyes.app import create_app


@pytest.fixture(scope='session')
def app():
    """
    Set up flask test app. [ This gets executed only once ]
    :return: Flask Test app
    """
    params = {
        'DEBUG': False,
        'TESTING': True
    }

    _app = create_app(settings_override=params)

    with _app.app_context():
        # Establish application context before running the test
        yield _app


@pytest.fixture(scope='function')
def client(app):
    """
    Set up an app test client. [ This gets set for each test function ]
    :param app:
    :return:
    """
    yield app.test_client()
