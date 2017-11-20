#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# abs(x)
print('abs of 10 is:', abs(10))
print('abs of -10 is:', abs(-10))
print('abs of 3+4j is:', abs(3+4j))

# all(iterable)
print('all of [0, 1, 2] is True?', all([0, 1, 2]))
print('all of [1, 2, 3] is True?', all([1, 2, 3]))

# any(iterable)
print('any of [0, 1, 2] is True?', any([0, 1, 2]))
print('any of [1, 2, 3] is True?', any([1, 2, 3]))
print('any of [0, 0, 0 ]is True?', any([0, 0, 0]))

# ascii(object)
print(ascii('ascii'))
print(ascii('\x23\x65'))
print(ascii('\u4e2d\u6587'))

# bin(x)
print('bin of 3 is:', bin(3))
print('bin of 10 is :', bin(-10))

# bool([x])
print('None to bool is:', bool())
print('0 to bool is:', bool(0))
print('number 10 to bool is:', bool(10))

# bytearray([source[, encoding[, errors]]])
print(bytearray([1, 2, 3, 4]))
print(bytearray('abc'.encode(encoding='utf-8')))
print(bytearray('中文'.encode(encoding='utf-8')))

# bytes([source[, encoding[, errors]]])
print(bytes('abc'.encode('utf-8')))

# callable(object)
print('Is the function callable?', callable(abs))

# chr(i)
for i in range(128):
    print(i, '-', chr(i), end='  ')

# ord(c)
for c in 'abcdefghigklmnopqrstuvwxyz':
    print(c, '-', ord(c), end='  ')

# classmethod(class)

# compile

# complex([real[, imag]])
print()
print(complex(1+2j))
print(complex('1+2j'))
print(complex(3))

# delattr

# dir | directory

# divmod
print(divmod(5, 2))
print(divmod(5.0, 2.0))

# enumerate(iterable, start=0)
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
print(enumerate(seasons))
print(list(enumerate(seasons)))

# eval(expression, globals=None, locals=None)
x = 2
print(eval('x**x'))

# exec(object[, globals[, locals]])
exec('print(x)')


# filter(function, iterable)
def iseven(x):
    return x % 2 == 0
l = filter(iseven, list(range(10)))
print(list(l))

# float
print(float('+1.23'))
print(float('   -12345\n'))
print('1e-003')
print('+1E5')
print(float('-Infinity'))

# format(value[, format_spec])
print(format(14, '#b'), format(14, 'b'))

# frozenset([iterable])

# getattr(object, name[, default])

# globals()
print(globals())

# hasattr(object, name)

# hash(object)
print(hash('life is short, use python.'))

# help([object])
print(help(abs))

# hex(x)
print(hex(255), hex(-34))

# id(object)
a, b = ('a', 'a')
print(id(a))
print(id(b))

# input()
# s = input('--> ')

# int(x=0)
print(int())
print(int('132', 8))

# isinstance(object, classinfo)
# issubclass(class, classinfo)
# iter(object[, sentinel])
# len()
# list()
# locals()
print(locals())

# map(function, iterable, ...)
# max(iterable, *[, key, default])
# max(arg1, arg2, *args[, key])
# memoryview(obj)

# min(iterable, *[, key, default])
# min(arg1, arg2, *args[, key])

# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# ord()
# pow(x, y[, z])
# print()
# property
# range(stop)
# range(start, stop[, step])
# reversed(seq)
print(reversed(list(range(10))))
print(list(reversed(list(range(10)))))
# round(number[, ndigits])
print(round(1.23333, 3))
# set()
# setattr()
# slice()
# sorted(iterable, *, key=None, reverse=False)
print(sorted([1, 2, 6, 9, 87, 5]))
# class str(object='')
# class str(object=b'', encoding='utf-8', errors='strict')

# sum(iterable[, start])

# tuple()
# class type(object)
# class type(name, bases, dict)
# vars([object])
class a:
    pass
print(vars(a))
# zip(*iterables)
print(zip([1, 2], [3, 4]))
# __import__