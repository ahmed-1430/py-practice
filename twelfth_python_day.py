"""My twelfth day practicing Python."""

import asyncio


async def greet():
    """Print an async greeting."""

    print("Hello from async Python!")


async def main():
    """Run the program."""

    await greet()


asyncio.run(main())