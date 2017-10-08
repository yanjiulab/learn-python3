#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use help([function_name]) to get a usage of function.
"""
x = abs(100)
y = abs(-20)
print(x, y)
print('max(1, 2, 3) =', max(1, 2, 3))
print('min(1, 2, 3) =', min(1, 2, 3))
print('sum([1, 2, 3]) =', sum([1, 2, 3]))

# alias function
a = abs     # variable a points function abs
print(a(-1))

# data type transformation
print(int('123'), int(12.34), float('12.34'), str(1.23), str(100), bool(1), bool(''))
