"""My twelfth day practicing Python."""

import asyncio


async def task(name, delay):
    """Run an async task."""

    print(f"{name} started.")

    await asyncio.sleep(delay)

    print(f"{name} completed.")


async def main():
    """Run async tasks."""

    await task("Task One", 1)
    await task("Task Two", 2)


asyncio.run(main())