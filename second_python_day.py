"""My second day practicing Python."""

print("Welcome to Python practice day 2!")
print("Today I am learning a little more about Python.")

student_name = "Ahmed"
learning_day = 2
print(f"I am {student_name}, and this is practice day {learning_day}.")

favorite_language = "python"
print(f"My favorite language is {favorite_language.title()}.")
print(f"In uppercase: {favorite_language.upper()}")

practice_tasks = ["read code", "write code"]
practice_tasks.append("run examples")
print("My practice tasks:", practice_tasks)

study_times = ("morning", "afternoon", "evening")
for study_time in study_times:
    print(f"I can study Python in the {study_time}.")

completed_tasks = 2
if completed_tasks >= 2:
    print("Great job! I completed my practice goal.")
else:
    print("I will keep practicing until I reach my goal.")
