"""My seventh day practicing Python."""

class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Introduce the person."""
        return f"My name is {self.name} and I am {self.age} years old."


person = Person("Ahmed", 24)

print("Python Practice Day 7")
print(person.introduce())