import csv
import json

# -----------------------------
# Step 1: Create and Write CSV
# -----------------------------
csv_data = [
    ["Name", "Age", "City"],
    ["Ali", 20, "Lahore"],
    ["Sara", 22, "Karachi"],
    ["Ahmed", 19, "Islamabad"],
    ["Ayesha", 23, "Lahore"]
]

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

print("CSV file created successfully.")

# -----------------------------
# Step 2: Read CSV and Filter
# -----------------------------
print("\nStudents from Lahore:")
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        if row["City"] == "Lahore":
            print(row)

# -----------------------------
# Step 3: Create and Write JSON
# -----------------------------
json_data = [
    {"Name": "Ali", "Age": 20, "City": "Lahore"},
    {"Name": "Sara", "Age": 22, "City": "Karachi"},
    {"Name": "Ahmed", "Age": 19, "City": "Islamabad"},
    {"Name": "Ayesha", "Age": 23, "City": "Lahore"}
]

with open("students.json", "w") as file:
    json.dump(json_data, file, indent=4)

print("\nJSON file created successfully.")

# -----------------------------
# Step 4: Read JSON and Filter
# -----------------------------
print("\nStudents older than 20:")
with open("students.json", "r") as file:
    data = json.load(file)
    for student in data:
        if student["Age"] > 20:
            print(student)
