#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

要创建一个set，需要提供一个list作为输入集合

这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。

要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：
"""

s1 = set([1, 1, 2, 2, 3, 3])
print(s1)
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)
s1.add(5)
print(s1)

# tuple with list
s2.add((1, 2, 3))
# s2.add((1, [2, 3]))       ---------->error
print(s2)
d = {
    (1, 2, 3): 'tuple'
    # (1, [2, 3]): 'tuple with list' -------->error
}
print(d)