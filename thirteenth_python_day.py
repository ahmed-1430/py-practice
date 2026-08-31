"""My thirteenth day practicing Python."""


def log_function(func):
    """Log function execution."""

    def wrapper():
        print(f"Running {func.__name__}...")

        func()

        print(f"{func.__name__} completed.")

    return wrapper


@log_function
def practice_python():
    """Practice Python."""

    print("Learning decorators!")


print("Python Practice Day 13")

practice_python()