# Simple Caesar Cipher

def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')

            # Shift character
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


# User input
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

# Encryption
encrypted = encrypt(message, shift)
print("Encrypted message:", encrypted)

# Decryption
decrypted = decrypt(encrypted, shift)
print("Decrypted message:", decrypted)
