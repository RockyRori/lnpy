# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 1, Question 1
"""
A bartender in a local bar makes a cup of cocktail using fruit juice and liquor in a ratio of 3ml of
fruit juice to 1ml of liquor. Write a program that prompts for (1) the cost of fruit juice per ml, (2) the cost
of liquor per ml, (3) the volume of a cup of cocktail (in terms of ml), and outputs the cost of a cup of
cocktail.
"""
from typing import Union


def cocktail_cost(fruit_juice_cost: Union[int, float], liquor_cost: Union[int, float], cocktail_volume: Union[int, float]) -> float:
    """
    calculate cocktail cost
    :param fruit_juice_cost: the cost of fruit juice per ml
    :param liquor_cost: the cost of liquor per ml
    :param cocktail_volume: the volume of a cup of cocktail in terms of ml
    :return: the cost of a cup of cocktail
    """
    if not (is_non_negative_number(fruit_juice_cost) and is_non_negative_number(liquor_cost)
            and is_non_negative_number(cocktail_volume)):
        raise Exception("wrong input")
    fruit_juice_volume = cocktail_volume * 3.0 / 4.0
    liquor_volume = cocktail_volume * 1.0 / 4.0
    return fruit_juice_volume * fruit_juice_cost + liquor_volume * liquor_cost


def is_non_negative_number(number: Union[int, float]) -> bool:
    """
    :param number: a variable being validated
    :return: number is either int or float and no less than 0
    """
    return isinstance(number, (int, float)) and number >= 0


if __name__ == '__main__':
    x, y, z = eval(input("Please input 3 number separately with comma interval"
                         " (fruit_juice_cost,liquor_cost,cocktail_volume):"))
    print(cocktail_cost(x, y, z))
