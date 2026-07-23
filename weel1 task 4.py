# --------------------------------------
# Function Library
# Temperature Converter + Area Calculator
# --------------------------------------

# Temperature Converter Functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


# Area Calculator Functions
def area_circle(radius):
    return 3.1416 * radius * radius

def area_rectangle(length, width):
    return length * width


# Main Program
print("===== FUNCTION LIBRARY =====")
print("1. Temperature Converter")
print("2. Area Calculator")

choice = int(input("Enter your choice (1 or 2): "))

if choice == 1:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    option = int(input("Enter your option: "))

    if option == 1:
        c = float(input("Enter temperature in Celsius: "))
        print("Temperature in Fahrenheit =", celsius_to_fahrenheit(c))

    elif option == 2:
        f = float(input("Enter temperature in Fahrenheit: "))
        print("Temperature in Celsius =", fahrenheit_to_celsius(f))

    else:
        print("Invalid option!")

elif choice == 2:
    print("\nArea Calculator")
    print("1. Circle")
    print("2. Rectangle")

    option = int(input("Enter your option: "))

    if option == 1:
        radius = float(input("Enter radius: "))
        print("Area of Circle =", area_circle(radius))

    elif option == 2:
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        print("Area of Rectangle =", area_rectangle(length, width))

    else:
        print("Invalid option!")

else:
    print("Invalid choice!")