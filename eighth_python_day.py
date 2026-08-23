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


def add_student(students, name, age, student_id):
    """Add a new student."""

    student = {
        "name": name,
        "age": age,
        "student_id": student_id,
        "grades": [],
    }

    students.append(student)


students = load_students()

add_student(
    students,
    "Sarah",
    22,
    "ST003",
)

save_students(students)

print("Python Practice Day 8")
print("Student added successfully.")

for student in students:
    print(
        f"{student['student_id']} - "
        f"{student['name']}"
    )