"""My eighth day practicing Python."""


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


def calculate_average(grades):
    """Calculate the average of grades."""

    if not grades:
        return 0

    return sum(grades) / len(grades)


def save_students_to_file(students):
    """Save students to a text file."""

    with open("students.txt", "w", encoding="utf-8") as file:
        for student in students:
            average = calculate_average(student["grades"])

            file.write(
                f"Name: {student['name']}\n"
                f"Age: {student['age']}\n"
                f"ID: {student['student_id']}\n"
                f"Grades: {student['grades']}\n"
                f"Average: {average:.2f}\n"
                f"{'-' * 30}\n"
            )


def read_students_file():
    """Read the student file."""

    with open("students.txt", "r", encoding="utf-8") as file:
        content = file.read()

    return content


print("Python Practice Day 8")

save_students_to_file(students)

content = read_students_file()

print("\nSaved File Content:")
print(content)