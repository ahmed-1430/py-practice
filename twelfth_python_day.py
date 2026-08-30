"""My twelfth day practicing Python."""

import asyncio

import aiohttp


async def get_github_user(session, username):
    """Fetch GitHub user data."""

    url = f"https://api.github.com/users/{username}"

    try:
        async with session.get(url) as response:
            if response.status != 200:
                print(
                    f"Could not fetch "
                    f"{username}"
                )
                return None

            return await response.json()

    except aiohttp.ClientError as error:
        print(
            f"Error fetching "
            f"{username}: {error}"
        )

        return None


async def main():
    """Fetch multiple users concurrently."""

    usernames = [
        "ahmed-1430",
        "torvalds",
        "octocat",
    ]

    timeout = aiohttp.ClientTimeout(total=10)

    async with aiohttp.ClientSession(
        timeout=timeout
    ) as session:
        tasks = [
            get_github_user(session, username)
            for username in usernames
        ]

        users = await asyncio.gather(*tasks)

        print("Python Practice Day 12")

        for user in users:
            if user:
                print(
                    f"{user['login']} - "
                    f"{user['followers']} followers"
                )


asyncio.run(main())