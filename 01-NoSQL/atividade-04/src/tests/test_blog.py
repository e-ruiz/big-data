import os
import tempfile
import pytest

import ..app
# from ..app import app

@pytest.fixture
def client():
    db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
    app.app.config['TESTING'] = True

    return app.app.test_client()

    # with app.app.test_client() as client:
    #     with app.app.app_context():
    #         app.init_db()
    #     yield client

    # os.close(db_fd)
    # os.unlink(app.app.config['DATABASE'])


def test_blog_get(client):
    res = client.get('/blogs/')
    assert res.status_code == 200


def test_blog_post(client):
    res = client.post('/blogs/')
    assert res.status_code == 200


