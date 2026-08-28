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
        """Return a description of the temperature."""

        if self.temperature >= 35:
            return "Very Hot"

        if self.temperature >= 30:
            return "Hot"

        if self.temperature >= 25:
            return "Warm"

        return "Cool"


    
    def display(self):
        """Display weather information."""

        print("\n" + "=" * 35)
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}°C")
        print(
            f"Temperature Status: "
            f"{self.get_temperature_status()}"
        )
        print(f"Condition: {self.condition}")
        print(f"Humidity: {self.humidity}%")
        print(f"Wind Speed: {self.wind_speed} km/h")
        print(
            f"Created: "
            f"{self.created_at:%Y-%m-%d %H:%M}"
        )
        print("=" * 35)


class WeatherTracker:
    """Manage weather data."""

    def __init__(self):
        self.weather_history = []

    def generate_weather(self, city):
        """Generate simulated weather data."""

        conditions = [
            "Sunny",
            "Cloudy",
            "Rainy",
            "Windy",
        ]

        weather = Weather(
            city=city.title(),
            temperature=random.randint(20, 38),
            condition=random.choice(conditions),
            humidity=random.randint(40, 95),
            wind_speed=random.randint(5, 30),
        )

        self.weather_history.append(weather)

        return weather

    def find_weather_by_city(self, city):
        """Find the latest weather data for a city."""

        for weather in reversed(self.weather_history):
            if weather.city.lower() == city.lower():
                return weather

        return None

    def show_history(self):
        """Display all weather records."""

        if not self.weather_history:
            print("\nNo weather history found.")
            return

        print("\nWEATHER HISTORY")

        for weather in self.weather_history:
            weather.display()





def main():
    """Run the Day 10 weather tracker."""

    print("=" * 40)
    print(" PYTHON WEATHER TRACKER")
    print("       PRACTICE DAY 10")
    print("=" * 40)

    tracker = WeatherTracker()

    cities = [
        "Dhaka",
        "Chattogram",
        "Khulna",
    ]

    while True:
        print("\n1. Generate Weather")
        print("2. Search City")
        print("3. View History")
        print("4. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            city = input("Enter city name: ").strip()

            if city:
                weather = tracker.generate_weather(city)
                print("\nWeather generated successfully.")
                weather.display()
            else:
                print("City name cannot be empty.")

        elif choice == "2":
            city = input("Enter city name: ").strip()

            weather = tracker.find_weather_by_city(city)

            if weather:
                weather.display()
            else:
                print("Weather data not found.")

        elif choice == "3":
            tracker.show_history()

        elif choice == "4":
            print("\nThanks for practicing Python!")
            break

        else:
            print("Invalid option. Please try again.")



if __name__ == "__main__":
    main()
