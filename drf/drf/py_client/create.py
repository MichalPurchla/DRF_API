import requests


endpoint = 'http://127.0.0.1:8000/api/products/'
endpoint2 = 'http://127.0.0.1:8000/api/products/second_method/'
data = {
    "title": 'this field is done',
    'price': 10.99
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())
