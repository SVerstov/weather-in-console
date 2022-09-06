import requests
from requests.models import Response
from typing import NamedTuple

import config
from exeptions import CantGetCoordinates


class Coordinates(NamedTuple):
    latitude: float
    longitude: float


def get_coords() -> Coordinates:
    """ returns current coordinates"""
    latitude = config.latitude
    longitude = config.longitude
    if not latitude or not longitude or config.GET_COORDS_BY_IP:
        return get_coords_by_ip()
    return Coordinates(latitude=_parse_float_coordinate(latitude),
                       longitude=_parse_float_coordinate(longitude))


def get_coords_by_ip() -> Coordinates:
    """ returns current coordinates using IP"""
    response_ip_info = requests.get(config.IPINFO_URL)
    if response_ip_info.status_code != 200:
        raise CantGetCoordinates
    return _parse_coords(response_ip_info)


def _parse_coords(ip_info: Response) -> Coordinates:
    try:
        latitude, longitude = ip_info.json()['loc'].split(',')
    except KeyError:
        raise CantGetCoordinates
    return Coordinates(latitude=_parse_float_coordinate(latitude),
                       longitude=_parse_float_coordinate(longitude))


def _parse_float_coordinate(value: str) -> float:
    try:
        return float(value)
    except ValueError:
        raise CantGetCoordinates
