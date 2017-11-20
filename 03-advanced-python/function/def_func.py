#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
def function_name([args]):
    pass
    return [data]
"""
import math


# Define my_abs function
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x


# Define a null function
def nothing():
    pass


# Define a function which return multiple values
def rtn_mul(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


if __name__ == '__main__':
    a, b = rtn_mul(100, 100, 60, math.pi / 6)
    print(a, b)
    t = rtn_mul(100, 100, 60, math.pi / 6)
    print('multiple value returned is actually a tuple:', t)