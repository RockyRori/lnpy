# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 1, Question 2
"""
A resident would like to calculate the amount of personal income tax he/she has to pay. Write
a program that prompts for (1) Total income, (2) Total deduction, (3) Total allowance and outputs the
amount of personal income tax he/she has to pay.
"""
from typing import Union


def tax_calculator(income: float, deduction: float, allowance: float) -> float:
    """
    calculate personal income tax
    :param income: a resident total income
    :param deduction: a resident total deduction
    :param allowance: a resident total allowance
    :return: the amount of personal income tax user has to pay
    """
    if not (is_non_negative_number(income) and is_non_negative_number(deduction)
            and is_non_negative_number(allowance)):
        raise Exception("wrong input")
    net_chargeable_income = income - deduction - allowance
    net_income = income - deduction

    # net income should not less than 0
    if net_income <= 0 or net_chargeable_income <= 0:
        net_income = tax_to_pay = 0
    elif 0 < net_chargeable_income <= 50000:
        tax_to_pay = net_chargeable_income * 0.02
    elif 50000 < net_chargeable_income <= 100000:
        tax_to_pay = (net_chargeable_income - 50000) * 0.06 + 1000
    elif 100000 < net_chargeable_income <= 150000:
        tax_to_pay = (net_chargeable_income - 100000) * 0.10 + 4000
    elif 150000 < net_chargeable_income <= 200000:
        tax_to_pay = (net_chargeable_income - 150000) * 0.14 + 9000
    else:
        tax_to_pay = (net_chargeable_income - 200000) * 0.17 + 16000
    # tax to pay should not more than tax limit
    tax_limit = net_income * 0.15
    tax_to_pay = tax_to_pay if tax_to_pay < tax_limit else tax_limit
    return tax_to_pay


def is_non_negative_number(number: Union[int, float]) -> bool:
    """
    :param number: a variable being validated
    :return: number is either int or float and no less than 0
    """
    return isinstance(number, (int, float)) and number >= 0


if __name__ == '__main__':
    x, y, z = eval(input("Please input 3 number separately with comma interval"
                         " (total income,total deduction,total allowance):"))
    print(tax_calculator(x, y, z))
