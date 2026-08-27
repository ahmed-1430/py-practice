"""My tenth day practicing Python."""

import random


cities = [
    "Dhaka",
    "Chattogram",
    "Khulna",
    "Rajshahi",
    "Sylhet",
]


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

    return {
        "city": city,
        "temperature": temperature,
        "condition": condition,
    }


print("Python Practice Day 10")

weather = get_weather("Dhaka")

print(f"City: {weather['city']}")
print(f"Temperature: {weather['temperature']}°C")
print(f"Condition: {weather['condition']}")