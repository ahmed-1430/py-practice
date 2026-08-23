"""My eighth day practicing Python."""

import json


def load_students():
    """Load students from JSON."""

    try:
        with open("students.json", "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []


def save_students(students):
    """Save students to JSON."""

    with open("students.json", "w", encoding="utf-8") as file:
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
    """Calculate grade average."""

    if not grades:
        return 0

    return sum(grades) / len(grades)


students = load_students()

add_grade(students, "ST001", 88)
add_grade(students, "ST001", 92)

save_students(students)

print("Python Practice Day 8")

student = find_student(students, "ST001")

if student:
    average = calculate_average(student["grades"])

    print(f"Name: {student['name']}")
    print(f"Grades: {student['grades']}")
    print(f"Average: {average:.2f}")