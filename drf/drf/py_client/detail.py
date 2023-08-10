import json

import requests


endpoint = 'http://127.0.0.1:8000/api/products/12'
endpoint2 = 'http://127.0.0.1:8000/api/products/second_method/1/'
auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
auth_response = requests.post(auth_endpoint, json={'username': 'admin',
                                                   'password': "admin"})
get_response = requests.get(endpoint, params={'id': 12}, headers={"Authorization": f"Token {auth_response.json()['token']}"})
print(get_response.json())


