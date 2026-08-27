"""My tenth day practicing Python."""

import random


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

    def get_temperature_status(self):
        """Return a temperature description."""

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
        print(
            f"Temperature Status: "
            f"{self.get_temperature_status()}"
        )
        print(f"Condition: {self.condition}")
        print(f"Humidity: {self.humidity}%")
        print(f"Wind Speed: {self.wind_speed} km/h")


def get_weather(city):
    """Generate weather information."""

    conditions = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Windy",
    ]

    return Weather(
        city=city,
        temperature=random.randint(20, 38),
        condition=random.choice(conditions),
        humidity=random.randint(40, 95),
        wind_speed=random.randint(5, 30),
    )


weather = get_weather("Dhaka")

print("Python Practice Day 10")
weather.display()