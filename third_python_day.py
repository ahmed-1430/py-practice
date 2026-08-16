"""My third day practicing Python."""


def square_number(number):
    """Return a number multiplied by itself."""
    return number * number


def is_even(number):
    """Return True when a number is even."""
    return number % 2 == 0


def calculate_average(numbers):
    """Return the average value of a list of numbers."""
    return sum(numbers) / len(numbers)


print("Welcome to Python practice day 3!")
print("Today I am learning about functions and return values.")

number_to_square = 6
squared_number = square_number(number_to_square)
print(f"The square of {number_to_square} is {squared_number}.")

practice_numbers = [1, 2, 3, 4, 5]
for practice_number in practice_numbers:
    if is_even(practice_number):
        print(f"{practice_number} is even.")
    else:
        print(f"{practice_number} is odd.")

practice_scores = [80, 90, 85]
average_score = calculate_average(practice_scores)
print(f"My average practice score is {average_score}.")
