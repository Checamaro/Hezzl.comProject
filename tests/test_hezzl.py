import pytest
import allure
import requests
from conftest import check_response_time



# Тест для метода Init
@allure.description("Метод INIT")
def test_init(api_data):
    response = requests.post("https://api-prod.hezzl.com/gw/v1/game/145602/init", json={})
    assert response.status_code == 200, "Expected status code 200"
    data = response.json().get("data", {})
    api_data["timeZone"] = data.get("time")
    assert data
    assert "auth" in data

# Тест для метода CheckLogin
@allure.description("Метод CheckLogin")
def test_check_login(api_data, check_response_time):
    response = requests.post("https://api-prod.hezzl.com/auth/v1/game/145602/check-login", json={"login": api_data["email"], "type": "email"})
    assert response.status_code == 200, "Expected status code 200"
    api_data["accessToken"] = response.json().get("accessToken")
    assert api_data["accessToken"]
    check_response_time(response)

# Тест для метода ConfirmCode
@allure.description("Метод ConfirmCode")
def test_confirm_code(api_data, check_response_time):
    response = requests.post("https://api-prod.hezzl.com/auth/v1/game/145602/check-login",
                             json={"login": api_data["email"], "type": "email"})
    api_data["accessToken"] = response.json().get("accessToken")
    response = requests.post("https://api-prod.hezzl.com/auth/v1/game/145602/confirm-code", headers={"Authorization": api_data["accessToken"]}, json={"code": api_data["password"]})
    assert response.status_code == 200, "Expected status code 200"
    check_response_time(response)


