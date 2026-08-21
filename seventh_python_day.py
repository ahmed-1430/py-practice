"""My seventh day practicing Python."""


class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name}."


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

    def introduce(self):
        return f"I am student {self.name}. My ID is {self.student_id}."

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    """Represent a teacher."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def introduce(self):
        return f"I am teacher {self.name}. I teach {self.subject}."


people = [
    Student("John", 21, "ST001"),
    Teacher("Sarah", 35, "Python"),
]

print("Python Practice Day 7")

for person in people:
    print(person.introduce())