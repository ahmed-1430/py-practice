"""My eleventh day practicing Python."""

import requests


def get_github_user(username):
    """Fetch GitHub user data safely."""

    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(
            url,
            timeout=10,
        )

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError:
        print("GitHub user not found.")

    except requests.exceptions.ConnectionError:
        print("Internet connection error.")

    except requests.exceptions.Timeout:
        print("Request timed out.")

    except requests.exceptions.RequestException as error:
        print(f"Something went wrong: {error}")

    return None


username = "ahmed-1430"

user = get_github_user(username)

print("Python Practice Day 11")

if user:
    print(f"Name: {user.get('name')}")
    print(f"Username: {user.get('login')}")
    print(f"Followers: {user.get('followers')}")