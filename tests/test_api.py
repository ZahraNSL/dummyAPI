import pytest
import requests

BASE_URL = "http://api:5000"

def test_valid_text():
    response = requests.post(f"{BASE_URL}/transform", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json()["transformed_text"] == "HELLO"

def test_missing_text_field():
    response = requests.post(f"{BASE_URL}/transform", json={})
    assert response.status_code == 400
    assert response.json()["error"] == "Missing \"text\" field"

def test_invalid_json():
    response = requests.post(f"{BASE_URL}/transform", data="not_json", headers={"Content-Type": "application/json"})
    assert response.status_code == 400