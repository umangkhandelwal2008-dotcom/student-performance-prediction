# -------------------------
# 1️⃣ Import Libraries
# -------------------------
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# -------------------------
# 2️⃣ Sample Dataset (You can replace with real CSV)
# -------------------------
data = {
    "Study_Hours": [2, 3, 4, 5, 1, 7, 8, 6, 9, 4],
    "Attendance": [70, 80, 85, 90, 60, 95, 96, 88, 98, 82],
    "Previous_Score": [50, 55, 60, 65, 40, 70, 75, 65, 80, 58],
    "Final_Marks": [55, 60, 65, 70, 45, 78, 85, 72, 90, 63]
}

df = pd.DataFrame(data)
print("Dataset:")
print(df.head())

# -------------------------
# 3️⃣ Split Features & Target
# -------------------------
X = df[["Study_Hours", "Attendance", "Previous_Score"]]
y = df["Final_Marks"]

# -------------------------
# 4️⃣ Train-Test Split
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------
# 5️⃣ Train Model
# -------------------------
model = LinearRegression()
model.fit(X_train, y_train)

# -------------------------
# 6️⃣ Predict on Test Data
# -------------------------
y_pred = model.predict(X_test)

# -------------------------
# 7️⃣ Model Evaluation
# -------------------------
print("\nModel Evaluation:")
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# -------------------------
# 8️⃣ Predict For New Student
# -------------------------
# Example: 5 study hours, 85% attendance, 60 previous score
new_data = np.array([[5, 85, 60]])
predicted_marks = model.predict(new_data)

print("\nPredicted Marks for Student:", predicted_marks[0])