import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
accuracy_score,
confusion_matrix,
precision_score,
recall_score,
f1_score,
classification_report
)
import pickle

# Load Dataset

df = pd.read_csv("student_project_100_rows.csv")

# Fill Missing Values

df = df.fillna(
df.mean(numeric_only=True)
)

# Features and Target

X = df.drop(
["Student_ID", "Result"],
axis=1
)

y = df["Result"]

# Train Test Split

X_train, X_test, y_train, y_test = train_test_split(
X,
y,
test_size=0.2,
random_state=42
)

# Train Model

model = RandomForestClassifier(
n_estimators=100,
random_state=42
)

model.fit(X_train, y_train)

# Predictions

y_pred = model.predict(X_test)

# Evaluation

print("Accuracy:", accuracy_score(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nPrecision:",
precision_score(y_test, y_pred, pos_label="Pass"))

print("Recall:",
recall_score(y_test, y_pred, pos_label="Pass"))

print("F1 Score:",
f1_score(y_test, y_pred, pos_label="Pass"))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Feature Importance

importance = pd.DataFrame({
"Feature": X.columns,
"Importance": model.feature_importances_
})

importance = importance.sort_values(
by="Importance",
ascending=False
)

print("\nFeature Importance:")
print(importance)

# Save Model

pickle.dump(
model,
open("student_model.pkl", "wb")
)

print("\nModel Saved Successfully!")
