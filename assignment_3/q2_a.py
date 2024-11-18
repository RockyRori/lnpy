# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 3, Question 2
"""
 In cryptography, a Caesar cipher is one of the simplest forms of substitution cipher.
The encryption is performed through shifting each letter in the plaintext forward by a number of positions
defined by the user along the alphabetical order. For example, if the user has defined the number
of forward position shift to be 4, every letter E in the plaintext will be replaced by A in the ciphertext
because character A is 4 positions in front of letter E in alphabetical order.
"""


def caesar_cipher(shift: int, plaintext: str) -> str:
    """
    encrypt message with alphabet shift
    :param shift: number of left shift
    :param plaintext: original text
    :return: encrypted text
    """
    encrypted_message = ""
    for char in plaintext:
        # Encrypt letters only
        if char.isalpha():
            # Preserve case sensitivity
            base = ord('A') if char.isupper() else ord('a')
            encrypted_message += chr((ord(char) - base - shift) % 26 + base)
        # Non-alphabetic characters remain unchanged
        else:
            encrypted_message += char
    return encrypted_message


if __name__ == "__main__":
    try:
        shift = int(input("Please enter the number of position shift: "))
        plaintext = input("Please enter the plaintext message: ")

        encrypted_message = caesar_cipher(shift, plaintext)
        print("The encrypted message is: ", encrypted_message)

    except ValueError:
        print("Invalid input! Please enter a valid integer for the shift.")
