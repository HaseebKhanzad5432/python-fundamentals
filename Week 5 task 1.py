import numpy as np
from collections import Counter

# Small 2D dataset
# Each point has two features: [x, y]
X = np.array([
    [1, 2],
    [2, 3],
    [3, 1],
    [6, 5],
    [7, 7],
    [8, 6]
])

# Labels: 0 = Class A, 1 = Class B
y = np.array([0, 0, 0, 1, 1, 1])


# Euclidean distance function
def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))


# KNN prediction function
def knn_predict(X, y, new_point, k=3):

    distances = []

    # Calculate distance from new point to every training point
    for i in range(len(X)):
        distance = euclidean_distance(X[i], new_point)
        distances.append((distance, y[i]))

    # Sort according to distance
    distances.sort(key=lambda x: x[0])

    # Select k nearest neighbors
    k_neighbors = distances[:k]

    # Get their labels
    labels = [label for distance, label in k_neighbors]

    # Majority voting
    prediction = Counter(labels).most_common(1)[0][0]

    return prediction, k_neighbors


# New point to classify
new_point = np.array([5, 4])

# Choose K
k = 3

# Make prediction
prediction, neighbors = knn_predict(X, y, new_point, k)

print("New Point:", new_point)
print("K:", k)
print("Nearest Neighbors:")

for distance, label in neighbors:
    print("Distance:", round(distance, 2), "Class:", label)

print("\nPredicted Class:", prediction)
