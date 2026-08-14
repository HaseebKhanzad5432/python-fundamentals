# Linear Regression with MAE, MSE and R²

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Small dataset
# X = Study Hours
# y = Exam Marks
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([35, 40, 50, 55, 65, 70])

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Make predictions
y_pred = model.predict(X)

# Evaluation metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Display results
print("Actual Values:     ", y)
print("Predicted Values:  ", y_pred)

print("\nEvaluation Results:")
print("MAE:", mae)
print("MSE:", mse)
print("R² Score:", r2)

# Model parameters
print("\nSlope:", model.coef_[0])
print("Intercept:", model.intercept_)
