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


def caesar_decipher(shift: int, ciphertext: str) -> str:
    """
    encrypt message with alphabet shift
    :param shift: number of left shift
    :param ciphertext: encrypted text
    :return: original text
    """
    decrypted_message = ""
    for char in ciphertext:
        # Decrypt letters only
        if char.isalpha():
            # Preserve case sensitivity
            base = ord('A') if char.isupper() else ord('a')
            decrypted_message += chr((ord(char) - base + shift) % 26 + base)
        # Non-alphabetic characters remain unchanged
        else:
            decrypted_message += char
    return decrypted_message


if __name__ == "__main__":
    try:
        shift = int(input("Please enter the number of position shift: "))
        ciphertext = input("Please enter the encrypted message: ")

        decrypted_message = caesar_decipher(shift, ciphertext)
        print("The decrypted message is: ", decrypted_message)

    except ValueError:
        print("Invalid input! Please enter a valid integer for the shift.")
