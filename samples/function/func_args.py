#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Arguments types: 必选参数、默认参数、可变参数、关键字参数和命名关键字参数
定义顺序： 必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
"""


# Location args
def power(x, n):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


# Default args
# NOTE: Default args are always behind required args
#       Default args must point to immutable object.
def power_def(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


def add_end(l=[]):
    l.append('END')
    return l


# Immutable args : numbers of args is not clearly. Args automatically form a tuple.
def calc(*numbers):
    sum_ = 0
    for n in numbers:
        sum_ = sum_ + n * n
    return sum_


# Keyword args : Args automatically form a dict.
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# Named keyword args : restrain the keywords.
# 如果没有可变参数，就必须加一个*作为特殊分隔符。
def person_restrain(name, age, *, city, job):
    print(name, age, city, job)


# Mixed args
def f1(a, b, c=0, *args, **kw):
    # 必选，必选，默认，可变，关键字
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    # 必选，必选，默认，命名关键字，关键字
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


def f3(a, b, c=0, *args, d, **kw):
    # 必选，必选，默认，可变，命名关键字，关键字
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'd =', d, 'kw =', kw)

if __name__ == '__main__':

    print(power(2, 2))

    print(power_def(2))
    print(add_end())
    print(add_end())
    print('default args must point immutable object!')

    print(calc(0))
    print(calc(1, 2, 3))
    list_ = [1, 2, 3, 4]
    print(calc(*list_))     # *list_ 代表将list的内容当做可变参数传入

    print(person('Bob', 21))
    print(person('Bob', 35, city='Beijing'))
    print(person('Adam', 45, gender='M', job='Engineer'))
    extra = {'city': 'Beijing', 'job': 'Engineer'}
    print(person('Bob', 24, **extra))

    # print(person_restrain('Jack', 24))    必须传入参数名
    print(person_restrain('Jack', 24, city='Beijing', job='Engineer'))

    # Mixed
    print(f1(1, 2))
    print(f1(1, 2, c=3))
    print(f1(1, 2, 3, 'a', 'b'))
    print(f1(1, 2, 3, 'a', 'b', x=99))
    print(f2(1, 2, d=99, ext=None))
    print(f3(1, 2, 3, 'a', 'b', d='name', x=99))

    args = (1, 2, 3, 4)
    kw = {'d': 99, 'x': '#'}
    print(f1(*args, **kw))
    args = (1, 2, 3)
    print(f2(*args, **kw))
    args = (1, 2, 3, 'a', 'b')
    kw = {'d': 'name', 'x': 99 }
    print(f3(*args, **kw))
