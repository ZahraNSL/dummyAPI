import responses
import requests

BASE_URL = "http://127.0.0.1:5000"

@responses.activate  # Decorator to mock HTTP calls
def test_mocked_api():
    responses.add(
        responses.POST,
        f"{BASE_URL}/transform",
        json={"transformed_text": "FAKE_RESPONSE"},
        status=200
    )

    response = requests.post(f"{BASE_URL}/transform", json={"text": "hello"})

    assert response.status_code == 200
    assert response.json()["transformed_text"] == "FAKE_RESPONSE"