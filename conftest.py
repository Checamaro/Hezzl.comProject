import pytest
import requests


@pytest.fixture
def api_data():
    return {
        "email": "test@hezzl.com",
        "password": "123456",
        "baseUrl": "https://api-prod.hezzl.com/",
        "campaignId": "145602",
        "accessToken": None,
        "timeZone": None
    }

@pytest.fixture
def check_response_time():
    def _check_response_time(response, max_time=200):
        response_time = response.elapsed.total_seconds() * 1000
        assert response_time < max_time, f"Response time {response_time}ms exceeded {max_time}ms"
    return _check_response_time