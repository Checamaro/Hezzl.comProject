import pytest
import allure
import requests
from conftest import check_response_time

# Тест для метода Init
@allure.description("Метод INIT")
def test_init(api_data):
    with allure.step("Отправка запроса на инициализацию"):
        response = requests.post("https://api-prod.hezzl.com/gw/v1/game/145602/init", json={})
    with allure.step("Проверка статуса кода"):
        assert response.status_code == 200, "Expected status code 200"
    with allure.step("Получение данных из ответа"):
        data = response.json().get("data", {})
        api_data["timeZone"] = data.get("time")
    with allure.step("Проверка наличия данных и параметра auth"):
        assert data
        assert "auth" in data


# Тест для метода CheckLogin
@allure.description("Метод CheckLogin")
def test_check_login(api_data, check_response_time):
    with allure.step("Отправка запроса на проверку логина"):
        response = requests.post("https://api-prod.hezzl.com/auth/v1/game/145602/check-login", json={"login": api_data["email"], "type": "email"})
    with allure.step("Проверка статуса кода"):
        assert response.status_code == 200, "Expected status code 200"
    with allure.step("Получение accessToken из ответа"):
        api_data["accessToken"] = response.json().get("accessToken")
    with allure.step("Проверка наличия accessToken"):
        assert api_data["accessToken"]
    with allure.step("Проверка времени ответа"):
        check_response_time(response)


# Тест для метода ConfirmCode
@allure.description("Метод ConfirmCode")
def test_confirm_code(api_data, check_response_time):
    with allure.step("Отправка запроса на проверку логина"):
        login_response = requests.post("https://api-prod.hezzl.com/auth/v1/game/145602/check-login", json={"login": api_data["email"], "type": "email"})
        api_data["accessToken"] = login_response.json().get("accessToken")
    with allure.step("Отправка запроса на подтверждение кода"):
        response = requests.post("https://api-prod.hezzl.com/auth/v1/game/145602/confirm-code", headers={"Authorization": api_data["accessToken"]}, json={"code": api_data["password"]})
    with allure.step("Проверка статуса кода"):
        assert response.status_code == 200, "Expected status code 200"
    with allure.step("Проверка времени ответа"):
        check_response_time(response)
