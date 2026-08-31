"""My thirteenth day practicing Python."""


def generate_numbers(start, end):
    """Generate numbers using yield."""

    current = start

    while current <= end:
        yield current
        current += 1


print("Python Practice Day 13")

for number in generate_numbers(1, 10):
    print(number)