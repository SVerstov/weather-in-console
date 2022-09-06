from coordinates import get_coords
from weather_api_service import get_weather
from weather_formatter import format_weather


def main():
    coordinates = get_coords()
    weather = get_weather(coordinates)
    print(format_weather(weather))


"""
5 day
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
"""
if __name__ == '__main__':
    main()
