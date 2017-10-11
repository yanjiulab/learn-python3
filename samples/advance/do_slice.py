#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
support data types : list, tuple, string.
 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1   0
"""
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

t = (1, 2, 3, 4)
print(t[:])

s = 'Python'
print(s[:])
