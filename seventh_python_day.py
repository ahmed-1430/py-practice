"""My seventh day practicing Python."""


class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        """Introduce the person."""
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


person = Person("Ahmed", 24)
student = Student("John", 21, "ST001")

print("Python Practice Day 7")
print(person.introduce())
print(student.introduce())
print(f"Student ID: {student.student_id}")