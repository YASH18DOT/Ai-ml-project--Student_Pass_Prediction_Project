import pickle
import pandas as pd

# Load Saved Model

loaded_model = pickle.load(
open("student_model.pkl", "rb")
)

# User Input

hours = float(input("Hours Studied: "))
attendance = float(input("Attendance: "))
assignments = float(input("Assignments: "))
previous_marks = float(input("Previous Marks: "))
class_test = float(input("Class Test Score: "))
project_score = float(input("Project Score: "))
sleep_hours = float(input("Sleep Hours: "))
participation = float(input("Participation: "))
internet_usage = float(input("Internet Usage: "))

# Create DataFrame

new_student = pd.DataFrame(
[[
hours,
attendance,
assignments,
previous_marks,
class_test,
project_score,
sleep_hours,
participation,
internet_usage
]],
columns=[
"Hours_Studied",
"Attendance",
"Assignments",
"Previous_Marks",
"Class_Test_Score",
"Project_Score",
"Sleep_Hours",
"Participation",
"Internet_Usage"
]
)

# Prediction

prediction = loaded_model.predict(
new_student
)

print("\nPrediction:", prediction[0])
