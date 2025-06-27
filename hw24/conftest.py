from requests.auth import HTTPBasicAuth
import requests
import pytest


BASE_URL= 'http://127.0.0.1:8080'

@pytest.fixture(scope='class')
def get_auth_cars_api_token():
    url = f"{BASE_URL}/auth"
    # username = "test_user",
    # password = "test_pass"
    response = requests.post(url= url, auth=HTTPBasicAuth(
        "test_user", # Якщо я вставляю параметр username, то отримую 401 , не знаю чому так
        "test_pass" # Якщо я вставляю параметр password, то отримую 401
    ))
    token = response.json().get("access_token")
    yield token

# def get_car_api(auth_token, sort_by=None, limit=None):
#     url = f"{BASE_URL}/cars"
#     headers = {
#         "Authorization": f"Bearer {auth_token}"
#     }
#     params = {
#         "sort_by": sort_by,
#         "limit": limit
#     }
#     response = requests.get(url=url, headers=headers, params=params)
#
#     return response

