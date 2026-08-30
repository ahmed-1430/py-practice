"""My twelfth day practicing Python."""

import asyncio

import aiohttp


async def get_github_user(session, username):
    """Fetch GitHub user data safely."""

    url = f"https://api.github.com/users/{username}"

    try:
        async with session.get(url) as response:
            if response.status == 404:
                print(f"User '{username}' not found.")
                return None

            if response.status != 200:
                print(
                    f"Request failed with "
                    f"status {response.status}"
                )
                return None

            return await response.json()

    except aiohttp.ClientError as error:
        print(f"Request error: {error}")
        return None


async def main():
    """Run the application."""

    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(
        timeout=timeout
    ) as session:
        user = await get_github_user(
            session,
            "ahmed-1430",
        )

        if user:
            print("Python Practice Day 12")
            print(f"Username: {user['login']}")
            print(f"Followers: {user['followers']}")


asyncio.run(main())