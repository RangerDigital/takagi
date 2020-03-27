import pytest
import requests

@pytest.fixture
def jwt_token(URL):
    payload = {"email": "me@gmail.com", "password": "Hello World"}
        
    response = requests.post(URL + "/users/login", json=payload)
    json = response.json()
        
    return json["jwt_token"]
    

@pytest.fixture
def poll_id(URL):
    payload = {"question": "Anon: Do you like it?", "options": ["Yes", "No"]}
    response = requests.post(URL + "/polls", json=payload)
    json = response.json()
        
    return json["_id"]

    
def test_create_anonymous_poll(URL):
    payload = {"question": "Anon: Do you like it?", "options": ["Yes", "No"]}
    
    response = requests.post(URL + "/polls", json=payload)
    json = response.json()
    
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    
    assert json["_id"]
    

def test_create_user_poll(URL, jwt_token):
    payload = {"question": "User: Do you like it?", "options": ["Yes", "No"]}
    
    response = requests.post(URL + "/polls", json=payload, headers={"Authorization": "Bearer " + jwt_token})
    json = response.json()
    
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    
    assert json["_id"]
    
    
def test_get_user_polls(URL, jwt_token):
    response = requests.get(URL + "/polls", headers={"Authorization": "Bearer " + jwt_token})
    json = response.json()
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    
    
def test_get_poll(URL, poll_id):
    response = requests.get(URL + "/polls/" + poll_id)
    json = response.json()
        
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    
    
def test_vote(URL, poll_id):
    payload = {"option_id": 0, "fingerprint": "Random Hash"}
    
    response = requests.post(URL + "/polls/" + poll_id + "/vote", json=payload)
    json = response.json()
        
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json"
    
    assert json["options"][0]["votes"] == 1
