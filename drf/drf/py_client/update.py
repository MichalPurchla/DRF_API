import requests


endpoint = 'http://127.0.0.1:8000/api/products/4/update/'

data = {
    'title': 'update12332141234',
    'price': 6.07
}
get_response = requests.put(endpoint, json=data)
print(get_response.json())