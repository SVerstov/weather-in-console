from coordinates import get_coords
from weather_api_service import get_weather
from weather_formatter import format_weather
from exeptions import CantGetCoordinates, ApiServiceError


def main():
    try:
        coordinates = get_coords()
    except CantGetCoordinates:
        print('Ошибка: Не удалось получить координаты')
        exit(1)

    try:
        weather = get_weather(coordinates)
    except ApiServiceError:
        print('Ошибка: Не удалось получить погоду')
        exit(1)

    print(format_weather(weather))


if __name__ == '__main__':
    main()
