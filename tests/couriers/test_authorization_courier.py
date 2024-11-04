import allure

from conftest import create_and_credentials_courier
from methods.courier_methods import CourierMethods
from data import delete_field, UNKNOWN_USER
from scooter_precondition.courier_precondition import setup_authorization_courier


class TestAuthorizationCouriers:
    @allure.title('Успешное авторизация курьера.')
    def test_authorization_courier_success(self, create_and_credentials_courier):
        courier_methods = CourierMethods()
        response = courier_methods.authorization_courier(
            setup_authorization_courier(create_and_credentials_courier)
        )
        assert response.status_code == 200 and response.json()['id']

    @allure.title('Попытка авторизоваться с неверным паролем.')
    def test_authorization_courier_invalid_password(self, create_and_credentials_courier):
        courier_methods = CourierMethods()
        create_and_credentials_courier['password'] = 'test_password'
        response = courier_methods.authorization_courier(create_and_credentials_courier)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Учетная запись не найдена"}

    @allure.title('Попытка авторизации без логина.')
    def test_authorization_no_login_courier(self, create_and_credentials_courier):
        courier_methods = CourierMethods()
        request_without_login = delete_field(create_and_credentials_courier, "login")
        response = courier_methods.authorization_courier(request_without_login)
        assert response.status_code == 400 and response.json() == {'code': 400, 'message': 'Недостаточно данных для входа'}

    @allure.title('Попытка авторизоваться под не существующего курьера.')
    def test_authorization_unknown_courier(self):
        courier_methods = CourierMethods()
        response = courier_methods.authorization_courier(UNKNOWN_USER)
        assert response.status_code == 404 and response.json() == {'code': 404, "message": "Учетная запись не найдена"}
