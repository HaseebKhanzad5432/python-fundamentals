import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# 1. Create a small 2D dataset
# -----------------------------
X = np.array([
    [1, 2], [1, 3], [2, 2], [2, 3],
    [8, 8], [9, 8], [8, 9], [9, 9],
    [4, 7], [5, 7], [4, 8], [5, 8]
])


# -----------------------------
# 2. K-Means from scratch
# -----------------------------
def kmeans(X, k, max_iterations=100):
    
    # Randomly select initial centroids
    random_indices = np.random.choice(len(X), k, replace=False)
    centroids = X[random_indices].copy()

    for _ in range(max_iterations):

        # Calculate distance from every point to every centroid
        distances = np.sqrt(
            ((X[:, np.newaxis] - centroids) ** 2).sum(axis=2)
        )

        # Assign each point to nearest centroid
        labels = np.argmin(distances, axis=1)

        # Calculate new centroids
        new_centroids = np.array([
            X[labels == i].mean(axis=0) if np.any(labels == i)
            else centroids[i]
            for i in range(k)
        ])

        # Stop if centroids do not change
        if np.allclose(centroids, new_centroids):
            break

        centroids = new_centroids

    # Calculate Within-Cluster Sum of Squares (WCSS)
    wcss = 0

    for i in range(k):
        cluster_points = X[labels == i]
        wcss += np.sum((cluster_points - centroids[i]) ** 2)

    return labels, centroids, wcss


# -----------------------------
# 3. Elbow Method
# -----------------------------
wcss_values = []

for k in range(1, 8):
    labels, centroids, wcss = kmeans(X, k)
    wcss_values.append(wcss)

# Plot Elbow Curve
plt.plot(range(1, 8), wcss_values, marker='o')
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS")
plt.title("Elbow Method")
plt.show()


# -----------------------------
# 4. Choose k
# -----------------------------
# From the elbow graph, suppose k = 3
best_k = 3

labels, centroids, wcss = kmeans(X, best_k)


# -----------------------------
# 5. Visualize final clusters
# -----------------------------
for i in range(best_k):
    cluster_points = X[labels == i]
    plt.scatter(
        cluster_points[:, 0],
        cluster_points[:, 1],
        label=f"Cluster {i + 1}"
    )

# Plot centroids
plt.scatter(
    centroids[:, 0],
    centroids[:, 1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()


# -----------------------------
# 6. Display results
# -----------------------------
print("Chosen k:", best_k)
print("Centroids:")
print(centroids)

print("\nCluster Labels:")
print(labels)

print("\nWCSS:", wcss)
