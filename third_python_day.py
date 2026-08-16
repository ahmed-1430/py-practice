"""My third day practicing Python."""


def square_number(number):
    """Return a number multiplied by itself."""
    return number * number


def is_even(number):
    """Return True when a number is even."""
    return number % 2 == 0


print("Welcome to Python practice day 3!")
print("Today I am learning about functions and return values.")

number_to_square = 6
squared_number = square_number(number_to_square)
print(f"The square of {number_to_square} is {squared_number}.")
