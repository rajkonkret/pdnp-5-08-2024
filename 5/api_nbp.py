import requests

# pip install requests
# HTTP GET

url = "https://api.nbp.pl/api/exchangerates/rates/A/USD/"
response = requests.get(url)
print(response)  # <Response [200]>
# 200 ok
# 3xx warningi
# 4xx - 404 - brak zasobu, 400 Bad Request - błedy po stroni eklienty
# 5xx - 500 Internal Server Error - błedy serwera
print(response.text)  # odczytanie jsona z odpowiedzi
# {"table": "A", "currency": "dolar amerykański", "code": "USD",
#  "rates": [{"no": "155/A/NBP/2024", "effectiveDate": "2024-08-09", "mid": 3.9604}]}
print(type(response.text))  # <class 'str'>
data = response.json()  # zamiana jsona na słownik
print(type(data))  # <class 'dict'>
print(data)
# {'table': 'A', 'currency': 'dolar amerykański', 'code': 'USD',
#  'rates': [{'no': '155/A/NBP/2024', 'effectiveDate': '2024-08-09', 'mid': 3.9604}]}
# klucze ze słownika
print(data.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
# wypisanie wartości dla klucza code
print(data['code'])  # USD
print(data['rates'])  # [{'no': '155/A/NBP/2024', 'effectiveDate': '2024-08-09', 'mid': 3.9604}]
print(type(data['rates']))  # <class 'list'>
print(data['rates'][0])  # {'no': '155/A/NBP/2024', 'effectiveDate': '2024-08-09', 'mid': 3.9604}
print(data['rates'][0]['mid'])  # 3.9604
