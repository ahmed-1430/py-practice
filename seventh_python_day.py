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

    total_students = 0

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

        Student.total_students += 1

    def introduce(self):
        return f"I am student {self.name}. My ID is {self.student_id}."

    def add_grade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True

        print("Grade must be between 0 and 100.")
        return False

    def average_grade(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)


def find_student(students, student_id):
    """Find a student by ID."""

    for student in students:
        if student.student_id == student_id:
            return student

    return None


students = [
    Student("Ahmed", 24, "ST001"),
    Student("John", 21, "ST002"),
    Student("Sarah", 22, "ST003"),
]

print("Python Practice Day 7")

student = find_student(students, "ST002")

if student:
    print("Student found:")
    print(student.introduce())
else:
    print("Student not found.")