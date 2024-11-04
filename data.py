import random
import string


BASE_URL_V1 = "https://qa-scooter.praktikum-services.ru/api/v1/"
COURIER_URL = 'courier/'
ORDERS_URL = 'orders/'

UNKNOWN_USER = {
    'login': 'test_login)))',
    'password': 'test_password))))'
}

ORDER_DATA_BLACK = {
    "firstName": "Auto_user-43",
    "lastName": "Ivanov",
    "address": "Konoha, 142 apt.",
    "metroStation": 1,
    "phone": "+7 800 355 35 55",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment",
    "color": [
        "BLACK"
    ]
}

ORDER_DATA_GREY = {
    "firstName": "Auto_user-49",
    "lastName": "Bobrov",
    "address": "Konoha, 142 apt.",
    "metroStation": 2,
    "phone": "+7 800 355 35 77",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment",
    "color": [
        "GREY"
    ]
}

ORDER_DATA_BLACK_AND_GREY = {
    "firstName": "Auto_user-55",
    "lastName": "Kopeykin",
    "address": "Konoha, 142 apt.",
    "metroStation": 3,
    "phone": "+7 800 355 35 88",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment",
    "color": [
        "BLACK",
        "GREY"
    ]
}

ORDER_DATA_NOT_COLOR = {
    "firstName": "Auto_user-55",
    "lastName": "Kopeykin",
    "address": "Konoha, 142 apt.",
    "metroStation": 3,
    "phone": "+7 800 355 35 88",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "test_comment",
}


def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def delete_field(payload, field):
    payload.pop(field)
    return payload
