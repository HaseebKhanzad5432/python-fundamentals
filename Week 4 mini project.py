# Marks Predictor & Pass/Fail Classifier

import numpy as np
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.metrics import accuracy_score, precision_score, recall_score

# -----------------------------
# Dataset
# -----------------------------
study_hours = np.array([1, 2, 2.5, 3, 4, 5, 5.5, 6, 7, 8, 9, 10]).reshape(-1, 1)
marks = np.array([35, 40, 45, 48, 55, 62, 65, 70, 75, 82, 88, 94])

# Pass = 1, Fail = 0
pass_fail = (marks >= 50).astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, marks, test_size=0.25, random_state=42
)

# -----------------------------
# 1. Regression Model
# -----------------------------
regression_model = LinearRegression()
regression_model.fit(X_train, y_train)

marks_prediction = regression_model.predict(X_test)

mae = mean_absolute_error(y_test, marks_prediction)
mse = mean_squared_error(y_test, marks_prediction)
r2 = r2_score(y_test, marks_prediction)

print("===== Marks Prediction (Regression) =====")
print("MAE:", round(mae, 2))
print("MSE:", round(mse, 2))
print("R² Score:", round(r2, 2))

# Predict marks for 7 study hours
new_hours = np.array([[7]])
predicted_marks = regression_model.predict(new_hours)

print("Predicted marks for 7 study hours:",
      round(predicted_marks[0], 2))


# -----------------------------
# 2. Pass/Fail Classifier
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    study_hours, pass_fail, test_size=0.25, random_state=42
)

classifier = LogisticRegression()
classifier.fit(X_train, y_train)

pass_fail_prediction = classifier.predict(X_test)

accuracy = accuracy_score(y_test, pass_fail_prediction)
precision = precision_score(y_test, pass_fail_prediction, zero_division=0)
recall = recall_score(y_test, pass_fail_prediction, zero_division=0)

print("\n===== Pass/Fail Classification =====")
print("Accuracy:", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))

# Predict pass/fail for 7 study hours
prediction = classifier.predict(np.array([[7]]))

if prediction[0] == 1:
    print("Prediction for 7 study hours: PASS")
else:
    print("Prediction for 7 study hours: FAIL")
