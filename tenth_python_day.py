"""My tenth day practicing Python."""

import random


cities = [
    "Dhaka",
    "Chattogram",
    "Khulna",
    "Rajshahi",
    "Sylhet",
]


def get_random_temperature():
    """Return a random temperature."""

    return random.randint(20, 38)


print("Python Practice Day 10")

city = random.choice(cities)
temperature = get_random_temperature()

print(f"City: {city}")
print(f"Temperature: {temperature}°C")