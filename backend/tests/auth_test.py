import pytest
import requests


def test_register(URL):
    payload = {"name": "John", "email": "me@gmail.com", "password": "Hello World"}

    response = requests.post(URL + "/users/register", json=payload)

    assert response.status_code == 204
    assert response.headers["Content-Type"] == "application/json"
    
    # Existing E-Mail
    response = requests.post(URL + "/users/register", json=payload)

    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    
    
def test_login(URL):
    payload = {"email": "me@gmail.com", "password": "Hello World"}
    
    response = requests.post(URL + "/users/login", json=payload)
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    
    assert json["jwt_token"]


def test_wrong_login(URL):
    payload = {"email": "me@gmail.com", "password": "Just Hello"}
    
    response = requests.post(URL + "/users/login", json=payload)
    json = response.json()

    assert response.status_code == 401
    assert response.headers["Content-Type"] == "application/json"
    
    assert not json.get("jwt_token")
