import allure

from data import delete_field
from methods.courier_methods import CourierMethods
from scooter_precondition.courier_precondition import setup_data_courier


class TestCreateCouriers:
    @allure.title('Успешное создание курьера.')
    def test_create_courier_success(self):
        courier_methods = CourierMethods()
        status_code, current_response = courier_methods.create_courier(setup_data_courier())
        assert status_code == 201 and current_response == {'ok': True}

    @allure.title('Попытка создать повторного курьера.')
    def test_create_double_courier(self):
        courier_methods = CourierMethods()
        first_courier = setup_data_courier()
        courier_methods.create_courier(first_courier)
        status_code, current_response = courier_methods.create_courier(first_courier)
        assert status_code == 409 and current_response == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

    @allure.title('Попытка создать курьера не имея логина.')
    def test_create_no_login_courier(self):
        courier_methods = CourierMethods()
        request_without_login = delete_field(setup_data_courier(), "login")
        status_code, current_response = courier_methods.create_courier(request_without_login)
        assert status_code == 400 and current_response == {'code': 400, 'message': 'Недостаточно данных для создания учетной записи'}

    @allure.title('Попытка создать курьера с ранее созданным логином.')
    def test_create_courier_repeat_login(self):
        courier_methods = CourierMethods()
        first_courier = setup_data_courier()
        courier_methods.create_courier(first_courier)
        login_courier = first_courier['login']
        second = setup_data_courier()
        second['login'] = login_courier
        status_code, current_response = courier_methods.create_courier(second)
        assert status_code == 409 and current_response == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}

