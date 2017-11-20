#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
list comprehension
"""
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

d = {'x': 'A',
     'y': 'B',
     'z': 'C'
     }
print([k + '=' + v for k, v in d.items()])

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

M = ['Hello', 'World', 'IBM', 18, 'Apple']
print('string only: ', [s.lower() for s in M if s and isinstance(s, str)])
print('all: ', [s.lower() if isinstance(s, str) else s for s in M])