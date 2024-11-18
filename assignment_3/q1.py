# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 3, Question 1
"""
In the past, the frequency analysis of letters was an important step in breaking cipher. Write a
Python program that prompt the user to input the path of a text file and output the occurrence count
of all 26 English alphabet (ignoring case) in the text file specified by the user.
"""
from collections import Counter
from typing import Dict


def read_text(path: str) -> str:
    content = ""
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"File \"{path}\" not found.")
    return content


def alphabet_frequency(data: str) -> Dict[str, int]:
    """
    count alphabet frequency from text file ignoring case
    :param data: original text from file
    :return: alphabet frequency dictionary
    """
    text = data.lower()
    letter_list = [char for char in text if char.isalpha()]
    return Counter(letter_list)


def ordering_print(data: Dict):
    """
    print dictionary in order
    :param data: any dictionary
    :return: console print
    """
    for key in sorted(data.keys()):
        print(f"'{key}': {data[key]}")


if __name__ == '__main__':
    # ./asg3_q1_sample.txt
    path_to_text = input("Please input a txt file path:")
    content = read_text(path_to_text)
    frequency_dict = alphabet_frequency(content)
    ordering_print(frequency_dict)
