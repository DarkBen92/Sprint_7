import pytest

from methods.courier_methods import CourierMethods
from scooter_precondition.courier_precondition import setup_data_courier, setup_authorization_courier


@pytest.fixture()
def create_and_credentials_courier():
    courier_methods = CourierMethods()
    courier_credentials = setup_data_courier()
    courier_methods.create_courier(courier_credentials)
    response = courier_methods.authorization_courier(courier_credentials)
    yield courier_credentials
    courier_methods.delete_courier(response.json()['id'])
