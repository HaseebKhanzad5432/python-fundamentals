# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"

# Main Program
while True:
    try:
        marks = float(input("Enter student marks (0-100): "))

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100.")

        grade = calculate_grade(marks)

        print("\n----- Result -----")
        print("Marks:", marks)
        print("Grade:", grade)
        break

    except ValueError as e:
        print("Invalid input:", e)
        print("Please try again.\n")
