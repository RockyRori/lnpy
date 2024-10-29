# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 2, Question 2
"""
Given two strings a and b consisting of lowercase characters. The task is to check whether two
given strings are an anagram of each other or not. An anagram of a string is another string that contains
the same characters, only the order of characters can be different. For example, act and tac are an
anagram of each other. You may assume that any input entered by the user would only contain
lowercase alphabets from a-z.
"""


def are_anagram(word_1: str, word_2: str) -> bool:
    """
    :param word_1: lowercase string
    :param word_2: another lowercase string
    :return: whether they are anagram
    """
    return sorted(word_1) == sorted(word_2)


if __name__ == '__main__':
    print(are_anagram(input("first string:"), input("second string:")))
