import pandas as pd
import random

data = []

for i in range(1, 101):

    hours = random.randint(1, 15)
    attendance = random.randint(50, 100)
    assignments = random.randint(30, 100)
    previous_marks = random.randint(30, 100)
    class_test = random.randint(30, 100)
    project_score = random.randint(30, 100)
    sleep_hours = random.randint(4, 9)
    participation = random.randint(1, 10)
    internet_usage = random.randint(1, 10)

    score = (
        hours * 2
        + attendance * 0.3
        + assignments * 0.2
        + previous_marks * 0.2
        + class_test * 0.2
        + project_score * 0.1
    )

    result = "Pass" if score > 70 else "Fail"

    if random.random() < 0.05:
        hours = None

    if random.random() < 0.05:
        attendance = None

    if random.random() < 0.05:
        assignments = None

    if random.random() < 0.05:
        previous_marks = None

    if random.random() < 0.05:
        class_test = None

    if random.random() < 0.05:
        project_score = None

    if random.random() < 0.05:
        sleep_hours = None

    if random.random() < 0.05:
        participation = None

    if random.random() < 0.05:
        internet_usage = None

    data.append([
        i,
        hours,
        attendance,
        assignments,
        previous_marks,
        class_test,
        project_score,
        sleep_hours,
        participation,
        internet_usage,
        result
    ])

df = pd.DataFrame(data, columns=[
    "Student_ID",
    "Hours_Studied",
    "Attendance",
    "Assignments",
    "Previous_Marks",
    "Class_Test_Score",
    "Project_Score",
    "Sleep_Hours",
    "Participation",
    "Internet_Usage",
    "Result"
])

df.to_csv(
    r"c:\Users\Dell\Desktop\Student_Pass_Prediction_Project\student_project_100_rows.csv",
    index=False
)

print("Dataset Created Successfully!")
print()
print("Rows :", len(df))
print("Columns :", len(df.columns))
print()
print(df.head())
print(df.tail())