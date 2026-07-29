import pandas as pd

# Step 1: Create a sample dataset
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Usman"],
    "Department": ["AI", "CS", "AI", "SE", "CS"],
    "Age": [21, 22, None, 23, 20],
    "Marks": [85, 90, 78, None, 88]
}

# Convert dictionary into DataFrame
df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# -----------------------------
# Step 2: Handle Missing Values
# -----------------------------

# Fill missing Age with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing Marks with 0
df["Marks"] = df["Marks"].fillna(0)

print("\nDataset After Handling Missing Values:")
print(df)

# -----------------------------
# Step 3: Filter Rows
# -----------------------------

# Students with Marks greater than 80
filtered_df = df[df["Marks"] > 80]

print("\nStudents with Marks > 80:")
print(filtered_df)

# -----------------------------
# Step 4: Group By Department
# -----------------------------

grouped = df.groupby("Department")["Marks"].mean()

print("\nAverage Marks by Department:")
print(grouped)
