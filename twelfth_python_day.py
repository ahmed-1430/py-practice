"""My twelfth day practicing Python."""

import asyncio

import aiohttp


async def get_github_user(
    session,
    username,
):
    """Fetch GitHub user data."""

    url = (
        f"https://api.github.com/"
        f"users/{username}"
    )

    async with session.get(url) as response:
        if response.status != 200:
            return None

        return await response.json()


async def get_repositories(
    session,
    username,
):
    """Fetch user repositories."""

    url = (
        f"https://api.github.com/"
        f"users/{username}/repos"
    )

    params = {
        "per_page": 100,
    }

    async with session.get(
        url,
        params=params,
    ) as response:
        if response.status != 200:
            return []

        return await response.json()


async def main():
    """Fetch profile and repositories concurrently."""

    username = "ahmed-1430"

    async with aiohttp.ClientSession() as session:

        user_task = get_github_user(
            session,
            username,
        )

        repo_task = get_repositories(
            session,
            username,
        )

        user, repositories = await asyncio.gather(
            user_task,
            repo_task,
        )

        print("Python Practice Day 12")

        if user:
            print(
                f"Username: "
                f"{user['login']}"
            )

        print(
            f"Repositories fetched: "
            f"{len(repositories)}"
        )


asyncio.run(main())