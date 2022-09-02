import os
from datetime import datetime
from enum import Enum
from typing import NamedTuple

import requests
from coordinates import Coordinates
from pydotenvs import load_env

load_env()

Celsius = float


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


class Weather(NamedTuple):
    temperature: Celsius
    weather_type: WeatherType
    weather_info: str
    sunrice: datetime
    sunset: datetime
    city: str

def get_weather(coordinates: Coordinates) -> Weather:
    pass

API_KEY = os.getenv('API_KEY')
lat = 60
lon = 30

weather_api = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&lang=ru&units=metric'
weather_info = requests.get(weather_api)
