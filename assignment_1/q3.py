# Student Name: LUO Suhai
# Student ID: 3160708

# Assignment 1, Question 3
"""
A student would like to calculate his/her term grade point average (GPA).
Write a program that reads a series of pairs of numbers as follows:
a) Credit (in terms of integer)
b) Grade point (in terms of floating-point number)
"""
from typing import Union


class Course:

    def __init__(self, credit: int = 0, grade_point: float = 0.0):
        super().__init__()
        self._credit: int = credit
        self._grade_point: float = grade_point

    @property
    def credit(self) -> int:
        return self._credit

    @property
    def grade_point(self) -> float:
        return self._grade_point


def gpa_calculator(courses: list[Course]) -> float:
    """
    calculate average grade point
    :param courses: a series of courses the student taken
    :return: gpa
    """
    weighted_grade_point = 0.0
    total_credit = 0.0
    for course in courses:
        weighted_grade_point += course.credit * course.grade_point
        total_credit += course.credit

    gpa = weighted_grade_point / total_credit if total_credit > 0 else 0
    return gpa


def is_non_negative_number(number: Union[int, float]) -> bool:
    """
    :param number: a variable being validated
    :return: number is either int or float and no less than 0
    """
    return isinstance(number, (int, float)) and number >= 0


if __name__ == '__main__':
    courses: list[Course] = []
    while True:
        c, gp = eval(input("Please input 2 number separately with comma interval and exit using negative input"
                           " (credit,grade_point):"))
        if not (is_non_negative_number(c) and is_non_negative_number(gp)):
            break
        courses.append(Course(c, gp))

    print(gpa_calculator(courses))
