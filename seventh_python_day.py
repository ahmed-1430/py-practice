"""My seventh day practicing Python."""


class Person:
    """Represent a person."""

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id
        self.grades = []

    def add_grade(self, grade):
        """Add a grade to the student."""
        self.grades.append(grade)

    def average_grade(self):
        """Calculate the average grade."""

        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)


class Teacher(Person):
    """Represent a teacher."""

    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        return f"{self.name} teaches {self.subject}."


student = Student("John", 21, "ST001")

student.add_grade(85)
student.add_grade(90)
student.add_grade(95)

print("Python Practice Day 7")
print(student.introduce())
print(f"Student ID: {student.student_id}")
print(f"Grades: {student.grades}")
print(f"Average: {student.average_grade():.2f}")