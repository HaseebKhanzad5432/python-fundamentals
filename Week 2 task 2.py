# Import NumPy
import numpy as np

# Create a NumPy array
arr = np.array([12, 25, 18, 30, 45, 50, 60, 75, 90, 100])

# Display the original array
print("Original Array:")
print(arr)

# -----------------------------
# Indexing
# -----------------------------
print("\nIndexing:")
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Fourth element:", arr[3])

# -----------------------------
# Slicing
# -----------------------------
print("\nSlicing:")
print("Elements from index 2 to 6:", arr[2:7])
print("First five elements:", arr[:5])
print("Last three elements:", arr[-3:])
print("Every second element:", arr[::2])

# -----------------------------
# Basic Statistics (No Loops)
# -----------------------------
print("\nBasic Statistics:")
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))

# -----------------------------
# Conditional Filtering
# -----------------------------
print("\nElements greater than 50:")
print(arr[arr > 50])
