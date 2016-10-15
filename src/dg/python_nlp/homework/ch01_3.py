# -*- coding: utf-8 -*-

import math


def factorial_sum(begin, end):
    target = range(begin, end)
    return sum(math.factorial(x) for x in target)

if __name__ == '__main__':
    print(factorial_sum(1, 4))
    print(factorial_sum(5, 10))

