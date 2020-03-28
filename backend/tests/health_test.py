import pytest
import requests


def test_health(URL):
    response = requests.get(URL + "/health")
    json = response.json()

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

    assert json["mongo_db"] == "success"
    assert json["redis_db"] == "success"
