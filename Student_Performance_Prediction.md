# Student Performance Prediction (Machine Learning Project)

This project predicts a student's final exam marks based on important
academic and lifestyle factors such as:

-   **Study hours**
-   **Attendance**
-   **Assignments completed**
-   **Sleep hours**
-   **Previous exam performance**

It uses **Python, Pandas, Scikit-Learn, and Linear Regression** to train
a machine-learning model and evaluate its performance.

## 🚀 Features

-   Clean and simple dataset (can be replaced with a real dataset)
-   Machine Learning model using **Linear Regression**
-   Evaluation metrics:
    -   **MAE** -- Mean Absolute Error
    -   **MSE** -- Mean Squared Error
    -   **RMSE** -- Root Mean Squared Error
-   Visualization of **Actual vs Predicted Marks**
-   Option to **predict marks for new students**

## 📁 Project Structure

    📂 Student-Performance-Prediction
    │── README.md
    │── student_performance.py
    │── requirements.txt (optional)

## 🛠️ Technologies Used

-   **Python 3.x**
-   **Pandas**
-   **NumPy**
-   **Scikit-Learn**
-   **Matplotlib**

## 🔧 Installation

    pip install numpy pandas scikit-learn matplotlib

## 📌 Usage

    python student_performance.py

The script will: - Load or create the dataset - Perform train-test
split - Train the ML model - Predict on test data - Print evaluation
scores - Plot a graph - Predict marks for a new student

## 📊 Sample Prediction (Example)

``` python
new_student = [[5, 90, 8, 7, 72]]
predicted_score = model.predict(new_student)
```

Output:

    Predicted marks for new student: 79.52

## 📈 Visualization

The script generates a graph comparing: - Actual Scores - Predicted
Scores

## 📚 Future Improvements

-   Add a larger real-life dataset
-   Use **Random Forest** or **Neural Networks**
-   Deploy the model on a **Flask / Django web app**
-   Add a **Tkinter GUI**
-   Hyperparameter tuning for better accuracy

## 🎯 Goal of the Project

To understand how multiple academic and behavioral factors impact a
student's performance, and how machine learning can be used to make
reliable predictions.
