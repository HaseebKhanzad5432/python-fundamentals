import pandas as pd

# Load CSV file
input_file = "messy_data.csv"
output_file = "cleaned_data.csv"
report_file = "summary_report.txt"

# Read CSV
df = pd.read_csv(input_file)

# Store original information
original_rows = len(df)
original_columns = len(df.columns)

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove extra spaces from string columns
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.strip().str.title()

# Count missing values before cleaning
missing_before = df.isnull().sum().sum()

# Fill missing values
for col in df.columns:
    if df[col].dtype == "object":
        df[col].fillna("Unknown", inplace=True)
    else:
        df[col].fillna(df[col].mean(), inplace=True)

# Remove duplicate rows
duplicates_removed = df.duplicated().sum()
df = df.drop_duplicates()

# Count missing values after cleaning
missing_after = df.isnull().sum().sum()

# Save cleaned CSV
df.to_csv(output_file, index=False)

# Create summary report
with open(report_file, "w") as report:
    report.write("DATA CLEANING SUMMARY REPORT\n")
    report.write("=" * 35 + "\n\n")
    report.write(f"Original Rows: {original_rows}\n")
    report.write(f"Original Columns: {original_columns}\n")
    report.write(f"Final Rows: {len(df)}\n")
    report.write(f"Duplicates Removed: {duplicates_removed}\n")
    report.write(f"Missing Values Before: {missing_before}\n")
    report.write(f"Missing Values After: {missing_after}\n")
    report.write("\nCleaning Performed:\n")
    report.write("- Standardized column names\n")
    report.write("- Removed duplicate rows\n")
    report.write("- Filled missing values\n")
    report.write("- Removed extra spaces\n")
    report.write("- Standardized text formatting\n")

print("Data cleaned successfully!")
print("Cleaned file saved as:", output_file)
print("Summary report saved as:", report_file)
