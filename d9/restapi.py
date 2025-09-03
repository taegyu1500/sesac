import requests
from urllib.parse import quote
import json

def request_country():
    country = input("Enter country name: ")
    API_URL = "https://restcountries.com/v3.1/name/"
    url = f"{API_URL}{quote(country)}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(json.dumps(data, indent=4))
    else:
        print("Error fetching country data.")

request_country()