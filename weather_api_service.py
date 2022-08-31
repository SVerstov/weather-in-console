import os
import requests

API_KEY = os.getenv('API_KEY')
weather_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=ru&units=metric'
weather_info = requests.get(weather_api)