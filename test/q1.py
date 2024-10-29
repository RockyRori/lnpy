# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 2, Question 1
"""
A palindrome is a number or text phrases that reads the same backwards as forwards. For example,
each of the following five-digit integers is a palindrome: 12321, 55555, 45554, and 11611.
Write a Python program that reads in a number or a text phrase as a string and determines whether
it is a palindrome. You may assume that any input entered by the user would only contain lowercase
alphabets from a-z and digits from 0-9.
"""


def is_palindrome(phase: str) -> bool:
    """
    :param phase: a number or a text
    :return: whether it is a palindrome
    """
    reverse = phase[::-1]
    return phase == reverse


if __name__ == '__main__':
    text = input("Please input a phase:")
    print(is_palindrome(text))
