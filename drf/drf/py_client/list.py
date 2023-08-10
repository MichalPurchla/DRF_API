import requests
from getpass import getpass


auth_endpoint = 'http://127.0.0.1:8000/api/auth/'
password = getpass()

auth_response = requests.post(auth_endpoint, json={'username': "test",
                                              "password": password})
print(auth_response.json())



endpoint = 'http://127.0.0.1:8000/api/products/'
endpoint2 = 'http://127.0.0.1:8000/api/products/second_method/'

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
