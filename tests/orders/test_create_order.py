import allure
import pytest

from data import ORDER_DATA_BLACK, ORDER_DATA_GREY, ORDER_DATA_BLACK_AND_GREY, ORDER_DATA_NOT_COLOR
from methods.order_methods import OrderMethods


class TestCreateOrder:
    @allure.title('Успешное создание заказа.')
    @pytest.mark.parametrize(
        'order_data',
        [
            ORDER_DATA_BLACK,
            ORDER_DATA_GREY,
            ORDER_DATA_BLACK_AND_GREY,
            ORDER_DATA_NOT_COLOR
        ]
    )
    def test_create_order_success(self, order_data):
        order_methods = OrderMethods()
        status_code,  current_response = order_methods.create_order(order_data)
        assert status_code == 201 and current_response['track']
