"""My eleventh day practicing Python."""

import requests


url = "https://api.github.com/users/ahmed-1430"

response = requests.get(url)

print("Python Practice Day 11")
print(response.status_code)
print(response.json())