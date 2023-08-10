import json

import requests


endpoint = 'http://127.0.0.1:8000/api/'

# get_response = requests.get(endpoint, params={'abc': 123}, json={'query': "Hello world"})
# print(type(get_response.json()))
# print(get_response.text)
# print(get_response.status_code)
# content = get_response.json()
# print(content['message'])


# get_response = requests.get(endpoint, json={"product_id": 123})
# content = get_response.json()
# print(type(content))
# print(content)

get_response = requests.post(endpoint, json={'title': 'Abc123', "content": 'hello world'})
print(get_response.json())
