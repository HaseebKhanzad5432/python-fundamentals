import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------
# 1. Training Data
# -----------------------------------
X = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([2, 4, 5, 8, 10], dtype=float)

# -----------------------------------
# 2. Initialize parameters
# -----------------------------------
w = 0.0       # slope
b = 0.0       # intercept

learning_rate = 0.01
epochs = 1000

n = len(X)

# -----------------------------------
# 3. Gradient Descent
# -----------------------------------
for i in range(epochs):

    # Prediction
    y_pred = w * X + b

    # Calculate gradients
    dw = (-2 / n) * np.sum(X * (y - y_pred))
    db = (-2 / n) * np.sum(y - y_pred)

    # Update parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db

# -----------------------------------
# 4. Final Model
# -----------------------------------
print("Slope (w):", w)
print("Intercept (b):", b)

print("Regression Equation:")
print(f"y = {w:.2f}x + {b:.2f}")

# -----------------------------------
# 5. Predictions
# -----------------------------------
y_pred = w * X + b

print("\nPredictions:")
for x, actual, predicted in zip(X, y, y_pred):
    print(f"X = {x}, Actual = {actual}, Predicted = {predicted:.2f}")

# -----------------------------------
# 6. Plot
# -----------------------------------
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_pred, label="Regression Line")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Simple Linear Regression using Gradient Descent")
plt.legend()
plt.show()
