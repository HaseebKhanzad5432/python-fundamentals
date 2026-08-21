# DBSCAN vs K-Means
# Using the same 2D dataset

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

# Same dataset
X = np.array([
    [1, 2], [1, 3], [2, 2], [2, 3],
    [8, 8], [9, 8], [8, 9], [9, 9],
    [4, 5], [5, 5], [4, 6], [5, 6]
])

# -----------------------------
# 1. K-Means
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans_labels = kmeans.fit_predict(X)

# -----------------------------
# 2. DBSCAN
# -----------------------------
dbscan = DBSCAN(eps=1.5, min_samples=2)
dbscan_labels = dbscan.fit_predict(X)

# -----------------------------
# 3. Display cluster labels
# -----------------------------
print("K-Means Cluster Labels:")
print(kmeans_labels)

print("\nDBSCAN Cluster Labels:")
print(dbscan_labels)

# -----------------------------
# 4. Plot K-Means
# -----------------------------
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=kmeans_labels,
    s=100
)
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200,
    label='Centroids'
)
plt.title("K-Means Clustering")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()

# -----------------------------
# 5. Plot DBSCAN
# -----------------------------
plt.subplot(1, 2, 2)
plt.scatter(
    X[:, 0],
    X[:, 1],
    c=dbscan_labels,
    s=100
)
plt.title("DBSCAN Clustering")
plt.xlabel("X")
plt.ylabel("Y")

plt.tight_layout()
plt.show()
