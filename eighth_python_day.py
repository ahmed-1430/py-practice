"""My eighth day practicing Python."""

import json


DATA_FILE = "students.json"


def load_students():
    """Load students from the JSON file."""

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        print("Student data is corrupted.")
        return []


def save_students(students):
    """Save students to the JSON file."""

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def find_student(students, student_id):
    """Find a student by ID."""

    for student in students:
        if student["student_id"] == student_id:
            return student

    return None


def add_student(students, name, age, student_id):
    """Add a new student."""

    if find_student(students, student_id):
        print("Student ID already exists.")
        return False

    students.append(
        {
            "name": name,
            "age": age,
            "student_id": student_id,
            "grades": [],
        }
    )

    return True


def add_grade(students, student_id, grade):
    """Add a grade to a student."""

    if not 0 <= grade <= 100:
        print("Grade must be between 0 and 100.")
        return False

    student = find_student(students, student_id)

    if student is None:
        print("Student not found.")
        return False

    student["grades"].append(grade)

    return True


def calculate_average(grades):
    """Calculate the average grade."""

    if not grades:
        return 0

    return sum(grades) / len(grades)


def get_status(average):
    """Return the student's academic status."""

    if average >= 80:
        return "Excellent"

    if average >= 60:
        return "Good"

    if average >= 40:
        return "Pass"

    return "Fail"


def show_student(student):
    """Display one student's information."""

    average = calculate_average(student["grades"])
    status = get_status(average)

    print("\n----------------------------")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Student ID: {student['student_id']}")
    print(f"Grades: {student['grades']}")
    print(f"Average: {average:.2f}")
    print(f"Status: {status}")
    print("----------------------------")


def show_all_students(students):
    """Display all students."""

    if not students:
        print("No students found.")
        return

    for student in students:
        show_student(student)


def main():
    """Run the student management system."""

    print("================================")
    print(" Python Practice Day 8")
    print(" Student Management System")
    print("================================")

    students = load_students()

    if not students:
        add_student(
            students,
            "Ahmed",
            24,
            "ST001",
        )

        add_student(
            students,
            "John",
            21,
            "ST002",
        )

        add_student(
            students,
            "Sarah",
            22,
            "ST003",
        )

        add_grade(students, "ST001", 90)
        add_grade(students, "ST001", 85)
        add_grade(students, "ST001", 95)

        add_grade(students, "ST002", 70)
        add_grade(students, "ST002", 65)
        add_grade(students, "ST002", 75)

        add_grade(students, "ST003", 45)
        add_grade(students, "ST003", 50)
        add_grade(students, "ST003", 55)

        save_students(students)

    print("\nAll Students")

    show_all_students(students)

    print("\nSearching for ST001")

    student = find_student(students, "ST001")

    if student:
        show_student(student)
    else:
        print("Student not found.")

    print("\nData is stored permanently in students.json.")


if __name__ == "__main__":
    main()