from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Literal

import requests
from requests import Response

from coordinates import Coordinates
from config import OPENWEATHER_URL
from exeptions import ApiServiceError

Celsius = float


class WeatherType(Enum):
    THUNDERSTORM = "Гроза"
    DRIZZLE = "Изморось"
    RAIN = "Дождь"
    SNOW = "Снег"
    CLEAR = "Ясно"
    FOG = "Туман"
    CLOUDS = "Облачно"


@dataclass(slots=True, frozen=True)
class Weather:
    temperature: Celsius
    weather_type: WeatherType
    weather_description: str
    sunrice: datetime
    sunset: datetime
    city: str


def get_weather(coordinates: Coordinates) -> Weather:
    openweather_response = _get_openweather_response(coordinates)
    weather = _parse_openweather_response(openweather_response)
    return weather


def _parse_openweather_response(openweather_response: Response) -> Weather:
    weather_dict = openweather_response.json()
    return Weather(
        temperature=_parse_temperature(weather_dict),
        weather_type=_parse_weather_type(weather_dict),
        weather_description=_parse_weather_info(weather_dict),
        sunrice=_parse_sun_time(weather_dict, time='sunrise'),
        sunset=_parse_sun_time(weather_dict, time='sunset'),
        city=_parse_cityname(weather_dict)
    )


def _get_openweather_response(coordinates: Coordinates) -> Response:
    url = OPENWEATHER_URL.format(latitude=coordinates.latitude, longitude=coordinates.longitude)
    response = requests.get(url)
    if response.status_code != 200:
        raise ApiServiceError
    return response


def _parse_temperature(weather_dict: dict) -> Celsius:
    temp = weather_dict['main']['temp']
    return round(float(temp), 1)


def _parse_weather_type(openweather_dict: dict) -> WeatherType:
    try:
        weather_type_id = str(openweather_dict["weather"][0]["id"])
    except (IndexError, KeyError):
        raise ApiServiceError
    weather_types = {
        "1": WeatherType.THUNDERSTORM,
        "3": WeatherType.DRIZZLE,
        "5": WeatherType.RAIN,
        "6": WeatherType.SNOW,
        "7": WeatherType.FOG,
        "800": WeatherType.CLEAR,
        "80": WeatherType.CLOUDS
    }
    for _id, _weather_type in weather_types.items():
        if weather_type_id.startswith(_id):
            return _weather_type
    raise ApiServiceError


def _parse_weather_info(weather_dict: dict) -> str:
    return weather_dict["weather"][0]["description"]


def _parse_sun_time(weather_dict, time: Literal["sunrise"] | Literal["sunset"]):
    return datetime.fromtimestamp(weather_dict['sys'][time])


def _parse_cityname(openweather_dict: dict) -> str:
    return openweather_dict["name"]
