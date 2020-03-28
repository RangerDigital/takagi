import pytest
import requests

@pytest.fixture
def jwt_token(URL):
    payload = {"email": "me@gmail.com", "password": "Hello World"}

    response = requests.post(URL + "/users/login", json=payload)
    json = response.json()

    return json["jwt_token"]


def test_get_user(URL, jwt_token):
    response = requests.get(URL + "/users/me", headers={"Authorization": "Bearer " + jwt_token})
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    assert json["name"] == "John"
    assert json["email"] == "me@gmail.com"

    assert not json.get("password")
    assert not json.get("salt")


def test_update_user(URL, jwt_token):
    payload = {"name": "Bob"}

    response = requests.patch(URL + "/users/me", json=payload, headers={"Authorization": "Bearer " + jwt_token})
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    assert json["name"] == "Bob"


def test_update_email(URL, jwt_token):
    payload = {"email": "me@gmail.com"}

    response = requests.patch(URL + "/users/me", json=payload, headers={"Authorization": "Bearer " + jwt_token})
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    assert json["email"] == "me@gmail.com"
