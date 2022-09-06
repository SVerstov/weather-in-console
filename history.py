import json
from datetime import datetime
from pathlib import Path
from typing import TypedDict

from weather_api_service import Weather
from abc import ABC, abstractmethod

from weather_formatter import format_weather


class WeatherStorage(ABC):
    """ Interface for any storage saving weather"""

    @abstractmethod
    def save(self, weather: Weather) -> None:
        pass


def save_weather(weather: Weather, storage: WeatherStorage) -> None:
    """ Save weather in the storage """
    storage.save(weather)


class PlainFileWeatherStorage(WeatherStorage):
    def __init__(self, file: Path):
        self._file = file

    def save(self, weather: Weather) -> None:
        now = datetime.now()
        formatted_weather = format_weather(weather)
        with open(self._file, 'a') as f:
            f.write(f"{now}\n{formatted_weather}\n")


class HistoryRecord(TypedDict):
    date: str
    weather: str


class JSONFileWeatherStorage(WeatherStorage):
    def __init__(self, jsonfile: Path):
        self._jsonfile = jsonfile
        self._init_storage()

    def save(self, weather: Weather) -> None:
        history = self._read_history()
        history.append({
            "date": str(datetime.now()),
            "weather": format_weather(weather)
        })
        self._write(history)

    def _init_storage(self):
        if not self._jsonfile.exists():
            self._jsonfile.write_text('[]')

    def _read_history(self) -> list[HistoryRecord]:
        with open(self._jsonfile, "r") as f:
            return json.load(f)

    def _write(self, history: list[HistoryRecord]) -> None:
        with open(self._jsonfile, "w") as f:
            json.dump(history, f, ensure_ascii=False, indent=4)
