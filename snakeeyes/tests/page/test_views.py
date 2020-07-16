from flask import url_for
from flask import Response


def test_home_page(client):
    response: Response = client.get(url_for('page.home'))
    assert response.status_code == 200


def test_terms_page(client):
    response: Response = client.get(url_for('page.terms'))
    assert response.status_code == 200


def test_privacy_page(client):
    response: Response = client.get(url_for('page.privacy'))
    assert response.status_code == 200
