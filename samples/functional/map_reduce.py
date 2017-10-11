#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
map:
reduce:
"""
from functools import reduce
print(help(map))


# map
def f(x):
    return x * x

l = list(range(10))
r = map(f, l)
print('r:', r, '\nlist of r:', list(r), '\ntypes of r: ', type(r))


# str2int
def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))

print(str2int('132456'))


# normalize
def normalize(name):
    return name.capitalize()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)


def prod(l):
    """
    calculate the product of items of d
    :param l: list
    :return: list
    """
    def p(x, y):
        return x * y
    return reduce(p, l)

L1 = [1, 2, 3, 4]
L2 = prod(L1)
print(L2)


def str2float(s):
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    int_str, float_str = s.split('.')
    return reduce(lambda x, y: x * 10 + y, map(char2num, int_str + float_str)) / (10 ** len(float_str))

Str = '123.465'
print(str2float(Str))


# 廖雪峰reduce代码
CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)

print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))



