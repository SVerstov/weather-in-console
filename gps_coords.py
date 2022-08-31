import os
import requests
from typing import NamedTuple
from pympler import asizeof

class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coords() -> Coordinates:
    """ Ruturns current coordinates"""
    latitude = os.getenv('latitude')
    longitude = os.getenv('longitude')
    if not latitude or not longitude:
        return get_coords_by_ip()
    return Coordinates(latitude=float(latitude),
                       longitude=float(longitude))


def get_coords_by_ip() -> Coordinates:
    location_info = requests.get('http://ipinfo.io/json')
    latitude, longitude = location_info.json()['loc'].split(',')
    return Coordinates(latitude=float(latitude),
                       longitude=float(longitude))