#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
在Python中，这种一边循环一边计算的机制，称为生成器：generator。
Two ways for generate generator:
1. use () instead [] in list comprehension.
2. 'yield' statement indicates this 'function-like' is generator, which saves algorithms rather than instances.
"""
s = (x * x for x in range(5))
print(s)
for x in s:
    print(x)


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)

# call generator manually:
g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


def yang_triangle():
    """
    # 期待输出:
    # [1]
    # [1, 1]
    # [1, 2, 1]
    # [1, 3, 3, 1]
    # [1, 4, 6, 4, 1]
    # [1, 5, 10, 10, 5, 1]
    # [1, 6, 15, 20, 15, 6, 1]
    # [1, 7, 21, 35, 35, 21, 7, 1]
    # [1, 8, 28, 56, 70, 56, 28, 8, 1]
    # [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
    """
    L = [1]
    while True:
        yield L
        L = [(L+[0])[i] + ([0]+L)[i] for i in range(len(L+[0]))]

# call generator manually:
n = 0
for t in yang_triangle():
    print(t)
    n = n + 1
    if n == 10:
        break

