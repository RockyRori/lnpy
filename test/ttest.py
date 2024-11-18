def caesar_cipher(shift, plaintext):
    encrypted_message = ""
    for char in plaintext:
        # Encrypt letters only
        if char.isalpha():
            # Preserve case sensitivity
            base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo
            encrypted_message += chr((ord(char) - base + shift) % 26 + base)
        else:
            # Non-alphabetic characters remain unchanged
            encrypted_message += char
    return encrypted_message


def main():
    try:
        # Prompt the user for inputs
        shift = int(input("Enter the number of forward position shifts: "))
        plaintext = input("Enter the plaintext message: ")

        # Encrypt the message
        encrypted_message = caesar_cipher(shift, plaintext)

        # Output the result
        print("Encrypted message:", encrypted_message)
    except ValueError:
        print("Invalid input! Please enter a valid integer for the shift.")


if __name__ == "__main__":
    main()
