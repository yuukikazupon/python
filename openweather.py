import requests
import json
from pprint import pprint

API_KEY = "7f8245b254aeb13ab693ad9e83a8d345"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?units=metric&lang=ja"
id = 1850147

response = requests.get(BASE_URL + "&id={}&APPID={}".format(id, API_KEY))
weather_data = json.loads(response.text)
pprint(weather_data)
pprint("東京の天気は"+weather_data['weather'][0]['description']+"です")
