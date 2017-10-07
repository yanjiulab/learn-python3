#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
loop statement include for, while, continue, and break.
"""

# Ues for loop print list:
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# Print numbers 0 - 9
for x in range(10):
    print(x)

# Ues while loop calculate the sum of 1-100
n = 100
t = 0
while n:
    t = t + n
    n = n - 1
print(t)

# continue : calculate the sum of odd numbers between 0 - 100
s = 0
for i in range(101):
    if i % 2 == 0:
        continue
    else:
        s = s + i
print(s)

# break
n = 1
while n <= 100:
    if n > 10:
        break   # break will ends up this loop
    print(n)
    n = n + 1
print('END')






