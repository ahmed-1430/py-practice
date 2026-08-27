"""My tenth day practicing Python."""

import random
from datetime import datetime


class Weather:
    """Represent weather information."""

    def __init__(
        self,
        city,
        temperature,
        condition,
        humidity,
        wind_speed,
    ):
        self.city = city
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.created_at = datetime.now()

    def get_temperature_status(self):
        """Return temperature status."""

        if self.temperature >= 35:
            return "Very Hot"

        if self.temperature >= 30:
            return "Hot"

        if self.temperature >= 25:
            return "Warm"

        return "Cool"

    def display(self):
        """Display weather information."""

        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Condition: {self.condition}")
        print(f"Humidity: {self.humidity}%")
        print(f"Wind Speed: {self.wind_speed} km/h")


weather_history = []


def get_weather(city):
    """Generate weather information."""

    conditions = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Windy",
    ]

    weather = Weather(
        city=city,
        temperature=random.randint(20, 38),
        condition=random.choice(conditions),
        humidity=random.randint(40, 95),
        wind_speed=random.randint(5, 30),
    )

    weather_history.append(weather)

    return weather


def find_weather_by_city(city):
    """Find weather data by city."""

    for weather in weather_history:
        if weather.city.lower() == city.lower():
            return weather

    return None


get_weather("Dhaka")
get_weather("Khulna")
get_weather("Sylhet")

print("Python Practice Day 10")

search_city = "Dhaka"

weather = find_weather_by_city(search_city)

if weather:
    print(f"\nWeather found for {search_city}")
    weather.display()
else:
    print("Weather data not found.")