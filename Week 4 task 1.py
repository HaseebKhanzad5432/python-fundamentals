import numpy as np

# Dataset
data = [10, 20, 30, 40, 50]

# -------------------------
# Calculate by hand
# -------------------------

# Mean
mean = sum(data) / len(data)

# Median
sorted_data = sorted(data)
n = len(sorted_data)

if n % 2 == 1:
    median = sorted_data[n // 2]
else:
    median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

# Variance (Population)
variance = sum((x - mean) ** 2 for x in data) / len(data)

# Standard Deviation
std_dev = variance ** 0.5

print("By-hand calculations:")
print("Mean =", mean)
print("Median =", median)
print("Variance =", variance)
print("Standard Deviation =", std_dev)


# -------------------------
# Verify using NumPy
# -------------------------

np_mean = np.mean(data)
np_median = np.median(data)
np_variance = np.var(data)
np_std_dev = np.std(data)

print("\nNumPy verification:")
print("Mean =", np_mean)
print("Median =", np_median)
print("Variance =", np_variance)
print("Standard Deviation =", np_std_dev)
