#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
key必须是不可变对象
"""
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}

print(d['Michael'])
d['Adam'] = 67
print(d)
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Bob'))
d.pop('Tracy')
print(d)

