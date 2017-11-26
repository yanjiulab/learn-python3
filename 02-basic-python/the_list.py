#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sequence Types — list (mutable)
列表是一种有序，可变的集合
"""

classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)

print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
print('len(classmates) =', len(classmates))

classmates.append('Adam')           # insert 'Adam' to the ends.
print('classmates =', classmates)
classmates.insert(1, 'Jack')        # insert 'Jack' to where index is 1
print('classmates =', classmates)
classmates.pop()                    # delete the last item.
print('classmates =', classmates)
classmates.pop(1)                   # delete the item[1]
print('classmates =', classmates)
classmates[1] = 'Tom'               # update the item[1]
print('classmates =', classmates)

