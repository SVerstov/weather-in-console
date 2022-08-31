from pydotenvs import load_env
from gps_coords import get_coords

def main:
    load_env()
    lat, lon = get_coords()
    weather = get_weather(lat,lon)
    print(format_weather(weather))



"""
5 day
api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}
"""
if __name__ == '__main__':
    main()