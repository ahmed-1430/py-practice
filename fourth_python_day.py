"""My fourth day practicing Python."""


def add_task(tasks, title):
    """Add a new unfinished task to a task list."""
    tasks.append({"title": title, "complete": False})


print("Welcome to Python practice day 4!")
print("Today I am building a small task-list program.")

my_tasks = []
add_task(my_tasks, "Read Python notes")
add_task(my_tasks, "Write a practice program")
