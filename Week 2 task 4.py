import pandas as pd

# Dataset 1: Student Information
students = {
    "Student_ID": [101, 102, 103, 104],
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"]
}

# Dataset 2: Student Marks
marks = {
    "Student_ID": [101, 102, 103, 104],
    "Marks": [85, 90, 78, 92]
}

# Create DataFrames
df_students = pd.DataFrame(students)
df_marks = pd.DataFrame(marks)

# Merge DataFrames on Student_ID
merged_df = pd.merge(df_students, df_marks, on="Student_ID")

# Display merged dataset
print("Merged Dataset:")
print(merged_df)

# Produce Summary
print("\nSummary:")
print("Total Students:", len(merged_df))
print("Average Marks:", merged_df["Marks"].mean())
print("Highest Marks:", merged_df["Marks"].max())
print("Lowest Marks:", merged_df["Marks"].min())
