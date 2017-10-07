#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。
用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：

由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
"""

# strings
l = 'life is short, '
w = "ues python!"
s = l + w
print(s)
for i in range(len(s)):
    print(s[i], end='')
print()
for i in s:
    print(i)

# single str
single_str = 'a'
print('\n%s is' % single_str, ord(single_str))
print('97 represents ', chr(97))
u_str = '\u4e2d\u6587'
print(u_str)

# str and bytes
o_str = 'ABC'
print(o_str, '\'s size is:', len(o_str))    # 返回字符数
print(o_str.encode('ascii'))
b_str = b'ABC'
print(b_str, '\'s length is:', len(b_str))  # 返回字节数

# 中文编码大小
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

# encode and decode
s = 'Python-中文'
print('s:', s)
print('type of s is:', type(s))
b = s.encode('utf-8')
print('b:', b)
print('type of b is:', type(b))
print('decode b is:', b.decode('utf-8'))

