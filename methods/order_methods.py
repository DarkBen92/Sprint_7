import allure
import requests
from data import BASE_URL_V1, ORDERS_URL


class OrderMethods:
    @allure.step('Cоздать заказ')
    def create_order(self, params):
        response = requests.post(f"{BASE_URL_V1}{ORDERS_URL}", json=params)
        return response.status_code, response.json()

    @allure.step('Получить заказ')
    def get_orders(self):
        response = requests.get(f"{BASE_URL_V1}{ORDERS_URL}")
        return response.status_code, response.json()
