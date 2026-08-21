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
        """Add a valid grade."""

        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True

        print("Grade must be between 0 and 100.")
        return False

    def average_grade(self):
        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)


student = Student("Ahmed", 24, "ST001")

student.add_grade(85)
student.add_grade(90)
student.add_grade(105)

print("Python Practice Day 7")
print(student.introduce())
print(f"Grades: {student.grades}")
print(f"Average: {student.average_grade():.2f}")