"""My thirteenth day practicing Python."""


def log_task(func):
    """Log task processing."""

    def wrapper(task):
        print(f"\nStarting task: {task}")

        result = func(task)

        print(f"Completed task: {task}")

        return result

    return wrapper


@log_task
def process_task(task):
    """Process a task."""

    return task.upper()


print("Python Practice Day 13")

task = "Learn Python Generators"

result = process_task(task)

print(f"Result: {result}")