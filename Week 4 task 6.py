import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# 1. Create a simple 2D dataset
X = np.array([
    [1, 1],
    [2, 2],
    [2, 1],
    [3, 2],
    [6, 6],
    [7, 7],
    [7, 6],
    [8, 7]
])

# Class labels
y = np.array([0, 0, 0, 0, 1, 1, 1, 1])

# 2. Train the classifier
model = LogisticRegression()
model.fit(X, y)

# 3. Create a grid of points
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

xx, yy = np.meshgrid(
    np.linspace(x_min, x_max, 200),
    np.linspace(y_min, y_max, 200)
)

# 4. Predict the class for every grid point
Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# 5. Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3)

# Plot data points
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    edgecolors="black"
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("Decision Boundary of Logistic Regression")
plt.show()
