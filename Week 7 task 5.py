import re

def validate_input(user_input):
    # Remove extra spaces
    user_input = user_input.strip()

    # Check if input is empty
    if not user_input:
        return False, "Input cannot be empty."

    # Limit input length
    if len(user_input) > 100:
        return False, "Input is too long."

    # Block suspicious patterns
    suspicious_patterns = [
        r"<script.*?>",       # Script tags
        r"</script>",         # Closing script tag
        r"javascript:",       # JavaScript URL
        r"\bDROP\s+TABLE\b",  # SQL DROP TABLE
        r"\bDELETE\s+FROM\b", # SQL DELETE
        r"\bUNION\s+SELECT\b",# SQL UNION SELECT
        r"--",                # SQL comment
        r";\s*--",            # Suspicious SQL pattern
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, user_input, re.IGNORECASE):
            return False, "Suspicious input detected."

    # Allow only letters, numbers, spaces and basic punctuation
    if not re.fullmatch(r"[A-Za-z0-9 .,!?'\-]+", user_input):
        return False, "Input contains invalid characters."

    return True, "Input is valid."


# Test the validator
test_inputs = [
    "Hello, how are you?",
    "My name is Haseeb.",
    "",
    "<script>alert('test')</script>",
    "DROP TABLE users",
    "Hello @#$%"
]

for text in test_inputs:
    valid, message = validate_input(text)
    print(f"Input: {text!r}")
    print(message)
    print("-" * 40)
