"""My thirteenth day practicing Python."""


class NumberIterator:
    """Create a simple custom iterator."""

    def __init__(self, start, end):
        self.current = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration

        number = self.current
        self.current += 1

        return number


print("Python Practice Day 13")

numbers = NumberIterator(1, 5)

for number in numbers:
    print(number)