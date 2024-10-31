import allure

from methods.order_methods import OrderMethods


class TestGetListOrders:
    @allure.title('Успешное получение заказов.')
    def test_get_list_orders(self):
        order_methods = OrderMethods()
        status_code, current_response = order_methods.get_orders()
        assert status_code == 200 and current_response['orders']
