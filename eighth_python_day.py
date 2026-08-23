"""My eighth day practicing Python."""

import json


students = [
    {
        "name": "Ahmed",
        "age": 24,
        "student_id": "ST001",
        "grades": [90, 85, 95],
    },
    {
        "name": "John",
        "age": 21,
        "student_id": "ST002",
        "grades": [70, 65, 75],
    },
]


def save_students_to_json(students):
    """Save students as JSON."""

    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


def read_students_from_json():
    """Read students from JSON."""

    with open("students.json", "r", encoding="utf-8") as file:
        return json.load(file)


print("Python Practice Day 8")

save_students_to_json(students)

loaded_students = read_students_from_json()

print("\nStudents loaded from JSON:")

for student in loaded_students:
    print(
        f"{student['name']} - "
        f"{student['student_id']}"
    )