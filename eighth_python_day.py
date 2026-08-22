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


print("Python Practice Day 8")

for student in students:
    average = calculate_average(student["grades"])

    print(
        f"{student['name']} - "
        f"Average: {average:.2f}"
    )