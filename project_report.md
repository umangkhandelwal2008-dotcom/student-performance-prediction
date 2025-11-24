# Project Report

## Student Performance Prediction Using Machine Learning

------------------------------------------------------------------------

## **1. Introduction**

Academic performance prediction is an important problem in the field of
education analytics. Predicting a student's marks in advance helps
teachers, parents, and schools identify students who need additional
support.

This project uses Machine Learning (ML) to predict a student's final
exam marks based on multiple input factors such as:

-   Study hours\
-   Attendance\
-   Assignments completed\
-   Sleep hours\
-   Previous marks

A **Linear Regression** model is used to understand how these factors
influence performance and to make accurate predictions.

------------------------------------------------------------------------

## **2. Problem Statement**

Students often underperform due to lack of timely evaluation and
guidance. Teachers need an automated system to identify students who may
score low and provide early intervention.

### **Objective:**

To develop an ML model that predicts a student's final marks using
measurable inputs such as hours of study, attendance percentage, sleep
duration, and prior performance.

------------------------------------------------------------------------

## **3. Objectives of the Project**

-   Collect or generate meaningful academic and lifestyle data of
    students.\
-   Preprocess and analyze the data using Python.\
-   Train a machine learning model that predicts final exam
    performance.\
-   Evaluate model performance using MAE, MSE, and RMSE metrics.\
-   Visualize results and compare actual vs predicted marks.

------------------------------------------------------------------------

## **4. Dataset Description**

A sample dataset of 15 students was created with the following features:

  Feature Name            Description
  ----------------------- ---------------------------------
  study_hours             Daily hours of study
  attendance              Attendance percentage in class
  assignments_completed   Number of completed assignments
  sleep_hours             Daily sleep duration (hours)
  previous_marks          Marks scored in previous exam
  final_marks             Actual final exam marks (label)

These factors are chosen because they directly impact academic
performance.

------------------------------------------------------------------------

## **5. Methodology**

The project follows the standard Machine Learning pipeline:

### **Step 1: Data Collection**

A synthetic dataset was created for training and testing purposes.

### **Step 2: Data Preprocessing**

-   Converted data to pandas DataFrame\
-   Identified features (X) and target label (y)\
-   Split data into train-test sets

### **Step 3: Model Selection**

**Linear Regression** selected because it is simple, interpretable, and
effective for numeric predictions.

### **Step 4: Model Training**

Model trained on 80% of the dataset.

### **Step 5: Testing & Evaluation**

Metrics used:\
- MAE\
- MSE\
- RMSE

### **Step 6: Visualization**

A graph was plotted comparing Actual vs Predicted marks.

------------------------------------------------------------------------

## **6. Technologies Used**

-   **Python**\
-   **Pandas**\
-   **NumPy**\
-   **Scikit-Learn**\
-   **Matplotlib**

------------------------------------------------------------------------

## **7. Implementation (Code Summary)**

The script includes:\
- Dataset creation\
- Train-test splitting\
- Training a Linear Regression model\
- Evaluation metrics\
- Visualization\
- New student prediction

(Full code provided earlier.)

------------------------------------------------------------------------

## **8. Results**

### ✔ **Model Evaluation**

The model performed well for the dataset.\
Typical results:\
- **MAE:** Low error\
- **RMSE:** Low deviation

### ✔ **Visualization**

Actual vs Predicted plot shows close alignment.

------------------------------------------------------------------------

## **9. Conclusion**

This project successfully demonstrates how Machine Learning can be used
to predict student performance based on academic and lifestyle
variables.

-   Study hours and previous marks had the highest impact.\
-   Linear Regression provided reliable predictions.\
-   The model can help identify weak students early.

------------------------------------------------------------------------

## **10. Future Scope**

Enhancements include:

-   Using a larger real dataset\
-   Advanced ML models (Random Forest, XGBoost, Neural Networks)\
-   Deploying as a web/mobile app\
-   Feature engineering\
-   Adding demographic features

------------------------------------------------------------------------

## **11. Applications**

-   School performance monitoring\
-   Early risk detection\
-   Personalized study planning

------------------------------------------------------------------------
