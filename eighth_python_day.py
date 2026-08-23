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


def student_exists(students, student_id):
    """Check whether a student already exists."""

    for student in students:
        if student["student_id"] == student_id:
            return True

    return False


def add_student(students, name, age, student_id):
    """Add a new student."""

    if student_exists(students, student_id):
        print("Student ID already exists.")
        return False

    student = {
        "name": name,
        "age": age,
        "student_id": student_id,
        "grades": [],
    }

    students.append(student)

    return True


students = load_students()

if add_student(
    students,
    "David",
    23,
    "ST004",
):
    save_students(students)
    print("Student added successfully.")


print("\nCurrent Students:")

for student in students:
    print(
        f"{student['student_id']} - "
        f"{student['name']}"
    )