"""
https://leetcode.com/problems/plus-one/submissions/
"""
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    length = len(digits)
    while length > 0:
        number = digits[length - 1]
        number += 1
        if number > 9:
            digits[length - 1] = 0
            length -= 1
            if length == 0:
                return [1] + digits
            continue
        digits[length - 1] = number
        break
    return digits


if __name__ == '__main__':
    print(plusOne([3, 9, 9, 9]))
