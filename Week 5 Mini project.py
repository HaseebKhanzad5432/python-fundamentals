# Mini Segmentation Project
# Student Study Habits / Quiz Scores using K-Means Clustering

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 1. Create a small dataset
data = {
    "Student": ["Ali", "Ahmed", "Hassan", "Usman", "Bilal",
                "Hamza", "Ayan", "Zain", "Saad", "Omer"],
    "Study_Hours": [2, 3, 2.5, 8, 7, 9, 4, 5, 3.5, 6],
    "Quiz_Score": [45, 50, 48, 85, 80, 92, 60, 65, 55, 75]
}

df = pd.DataFrame(data)

# 2. Select features for clustering
X = df[["Study_Hours", "Quiz_Score"]]

# 3. Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["Cluster"] = kmeans.fit_predict(X)

# 4. Display students with their clusters
print("Student Segmentation:")
print(df)

# 5. Display cluster centers
print("\nCluster Centers:")
print(kmeans.cluster_centers_)

# 6. Plot the clusters
plt.figure(figsize=(8, 5))

plt.scatter(
    df["Study_Hours"],
    df["Quiz_Score"],
    c=df["Cluster"],
    s=100
)

# Add student names
for i in range(len(df)):
    plt.text(
        df["Study_Hours"][i] + 0.1,
        df["Quiz_Score"][i],
        df["Student"][i]
    )

plt.xlabel("Study Hours")
plt.ylabel("Quiz Score")
plt.title("Student Segmentation using K-Means")
plt.show()

# 7. Create cluster profiles
for cluster in sorted(df["Cluster"].unique()):
    group = df[df["Cluster"] == cluster]

    avg_hours = group["Study_Hours"].mean()
    avg_score = group["Quiz_Score"].mean()

    print(
        f"Cluster {cluster}: "
        f"Average Study Hours = {avg_hours:.1f}, "
        f"Average Quiz Score = {avg_score:.1f}"
    )
