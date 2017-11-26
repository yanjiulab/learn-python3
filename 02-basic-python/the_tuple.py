#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sequence Types — tuple (immutable)
元组是一种有序，不可变的集合, 不可变指的是指向不变。
"""
# 没有pop, insert 等方法，也不能赋值，其他的方法和list相同
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates[-1])

# 定义一个元素的元组
t = (1)             # define an integer
print(type(t))
t = (1, )           # define a tuple
print(type(t))

# 指向不变
t = ('a', 'b', ['x', 'y'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)
