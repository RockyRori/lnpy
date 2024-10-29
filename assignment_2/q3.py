# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 2, Question 3
"""
A prime integer is any integer larger than 1 that is divisible only by itself and 1. The Sieve of
Eratosthenes is a method of finding prime numbers. It operates as follows:
• Create a list with all elements initialised to 1.
• Starting with list[2], every time when an element X is found to be equal to 1, loop through the
remaining element in the list and assign zero to every element with an index being the multiple of the
index of X.

When this process is complete, any element with an index larger than 1 that still have a value of 1 indicate
that its index is a prime number. The indices of these element can then be printed. (i.e. if list[2] equals
to 1 after process is complete, then 2 is a prime number and should be printed) Write a program that
uses a list of 1000 elements to determine and print the prime number between 1 and 999.

For example, element list[2] equals to 1, all elements in the list having indexes being multiples of
2 and larger than 2 (i.e. list[4], list[6], list[8], list[10], …) will be set to zero. Element
list[3] equals to 1, all elements in the list having indexes being multiples of 3 and larger than 3 (i.e.
list[6], list[9], list[12], list[15], …) will be set to zero; and so on.
"""


def prime_list(end: int) -> list:
    """
    :param end: the scale of prime list
    :return: complete prime list
    """
    p_list = [1] * end
    for i in range(2, int(end / 2) + 1, 1):
        if p_list[i] == 1:
            for n in range(i, end, i):
                p_list[n] = 0
            p_list[i] = 1
    return p_list


if __name__ == '__main__':
    print(prime_list(1000))
