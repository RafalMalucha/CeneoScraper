import requests

url = "https://www.ceneo.pl/105186036#tab=reviews"
response = requests.get(url)
print(response.status_code) 