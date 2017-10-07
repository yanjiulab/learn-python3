#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
if statement has three structures.
"""

# if
age = 20
if age >= 18:
    print('your age is', age)
    print('adult')

# if...else...
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
else:
    print('your age is', age)
    print('teenager')

# if...elif...elif...else
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# tips --'if x' is better than 'if x == True'
if age:
    print('true')


