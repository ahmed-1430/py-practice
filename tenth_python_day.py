"""My tenth day practicing Python."""

import random


class Weather:
    """Represent weather information."""

    def __init__(self, city, temperature, condition):
        self.city = city
        self.temperature = temperature
        self.condition = condition

    def display(self):
        """Display weather information."""

        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}°C")
        print(f"Condition: {self.condition}")


def get_weather(city):
    """Generate weather information."""

    temperature = random.randint(20, 38)

    conditions = [
        "Sunny",
        "Cloudy",
        "Rainy",
        "Windy",
    ]

    condition = random.choice(conditions)

    return Weather(
        city,
        temperature,
        condition,
    )


print("Python Practice Day 10")

weather = get_weather("Dhaka")

weather.display()