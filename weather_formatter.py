from weather_api_service import Weather


def format_weather(weather: Weather) -> str:
    return f"{weather.city}\n" \
           f"{weather.weather_description}, {weather.temperature}°C\n" \
           f"Восход: {weather.sunrice.strftime('%H:%M')}\n" \
           f"Закат: {weather.sunset.strftime('%H:%M')}\n"
