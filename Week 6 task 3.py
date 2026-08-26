import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import make_pipeline
from sklearn.metrics import mean_squared_error

# Toy dataset
np.random.seed(42)

X = np.linspace(0, 10, 30)
y = np.sin(X) + np.random.normal(0, 0.15, 30)

X = X.reshape(-1, 1)

# Split into training and testing data
X_train = X[:20]
y_train = y[:20]

X_test = X[20:]
y_test = y[20:]

degrees = range(1, 16)
train_errors = []
test_errors = []

# Train polynomial models of different complexity
for degree in degrees:
    model = make_pipeline(
        PolynomialFeatures(degree),
        LinearRegression()
    )

    model.fit(X_train, y_train)

    train_pred = model.predict(X_train)
    test_pred = model.predict(X_test)

    train_errors.append(mean_squared_error(y_train, train_pred))
    test_errors.append(mean_squared_error(y_test, test_pred))

# Plot train error vs test error
plt.figure(figsize=(10, 6))

plt.plot(degrees, train_errors, marker='o', label='Train Error')
plt.plot(degrees, test_errors, marker='o', label='Test Error')

plt.xlabel("Model Complexity (Polynomial Degree)")
plt.ylabel("Mean Squared Error")
plt.title("Underfitting vs. Overfitting")
plt.legend()
plt.grid(True)
plt.show()

# Print interpretation
print("Low degree  → Underfitting")
print("Middle degree → Good fit")
print("High degree → Overfitting")
