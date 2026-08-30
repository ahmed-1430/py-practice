"""My twelfth day practicing Python."""

import asyncio

import aiohttp


async def get_github_user(username):
    """Fetch GitHub user data asynchronously."""

    url = f"https://api.github.com/users/{username}"

    async with aiohttp.ClientSession() as session:
        async with session.get(
            url,
            timeout=aiohttp.ClientTimeout(total=10),
        ) as response:
            return await response.json()


async def main():
    """Run the async API request."""

    user = await get_github_user("ahmed-1430")

    print("Python Practice Day 12")
    print(f"Username: {user.get('login')}")
    print(f"Name: {user.get('name')}")
    print(f"Followers: {user.get('followers')}")


asyncio.run(main())