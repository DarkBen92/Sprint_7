import requests

from data import generate_random_string


def setup_data_courier():
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    return payload


def setup_authorization_courier(data_courier):
    payload = {
        "login": data_courier["login"],
        "password": data_courier["password"],
    }
    return payload
