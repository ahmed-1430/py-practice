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
        """Add a valid grade."""

        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True

        print(f"Invalid grade: {grade}")
        return False

    def average_grade(self):
        """Calculate the average grade."""

        if not self.grades:
            return 0

        return sum(self.grades) / len(self.grades)

    def get_status(self):
        """Return the student's academic status."""

        average = self.average_grade()

        if average >= 80:
            return "Excellent"
        if average >= 60:
            return "Good"
        if average >= 40:
            return "Pass"

        return "Fail"


def find_student(students, student_id):
    """Find a student by ID."""

    for student in students:
        if student.student_id == student_id:
            return student

    return None


def show_student_report(student):
    """Display one student's report."""

    print("\n-------------------------")
    print(f"Name: {student.name}")
    print(f"Age: {student.age}")
    print(f"Student ID: {student.student_id}")
    print(f"Grades: {student.grades}")
    print(f"Average: {student.average_grade():.2f}")
    print(f"Status: {student.get_status()}")
    print("-------------------------")


def main():
    """Run the Day 7 OOP practice."""

    print("Welcome to Python practice day 7!")
    print("Today I am practicing inheritance and polymorphism.")

    students = [
        Student("Ahmed", 24, "ST001"),
        Student("John", 21, "ST002"),
        Student("Sarah", 22, "ST003"),
    ]

    students[0].add_grade(90)
    students[0].add_grade(85)
    students[0].add_grade(95)

    students[1].add_grade(70)
    students[1].add_grade(65)
    students[1].add_grade(75)

    students[2].add_grade(45)
    students[2].add_grade(50)
    students[2].add_grade(55)

    print(f"\nTotal students: {Student.total_students}")

    print("\nAll Students")

    for student in students:
        print(student.introduce())

    print("\nSearching for ST002")

    found_student = find_student(students, "ST002")

    if found_student:
        show_student_report(found_student)
    else:
        print("Student not found.")

    print("\nComplete Student Reports")

    for student in students:
        show_student_report(student)


if __name__ == "__main__":
    main()