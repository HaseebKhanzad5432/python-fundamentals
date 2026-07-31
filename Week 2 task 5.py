import logging

# Configure logging
logging.basicConfig(
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Custom Exception Class
class InvalidAgeError(Exception):
    """Raised when the age is invalid."""
    pass


def check_age(age):
    if age < 0:
        raise InvalidAgeError("Age cannot be negative.")
    elif age < 18:
        raise InvalidAgeError("Age must be at least 18.")
    else:
        return "Access Granted"


try:
    age = int(input("Enter your age: "))
    result = check_age(age)
    print(result)

except InvalidAgeError as e:
    logging.error(e)

except ValueError:
    logging.error("Invalid input! Please enter a valid number.")
