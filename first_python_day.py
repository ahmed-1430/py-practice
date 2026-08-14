"""My first day practicing Python."""


def say_hello(name):
    """Print a friendly greeting."""
    print(f"Hello, {name}!")


print("Hello, Python!")
print("Today I am coding Python for the first time.")

student_name = "Ahmed"
learning_day = 1
say_hello(student_name)
print(f"My name is {student_name}, and this is Python day {learning_day}.")

first_number = 10
second_number = 5
total = first_number + second_number
print(f"{first_number} + {second_number} = {total}")

favorite_topics = ["variables", "numbers", "lists"]
print("Topics I am learning:", favorite_topics)

for topic in favorite_topics:
    print(f"I will practice {topic} today.")

is_practicing_today = True
if is_practicing_today:
    print("I am making progress by practicing every day!")
else:
    print("I will practice again tomorrow.")
