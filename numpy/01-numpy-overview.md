Numpy简介
=========
The Basics
----------
Numpy主要对象是齐次多维数组。
- 元素(element):类型一致，使用正整数下标索引。
- 轴(axes):Numpy的维(dimensions)称为坐标。
- 维度(rank):Numpy的维的个数称为维度。

Numpy的数组类叫做`narray`，也被称为`array`，`numpy.array`与`array.array`不同。
- ndarray.ndim 数组维度
- ndarray.shape 数组形状
- ndarray.size 数组元素个数（数组长度）
- ndarray.dtype 数组元素数据类型
- ndarray.itemsize 数组元素类型大小
- ndarray.data 数组元素（基本不用，通常用下标索引访问数据）

```python
>>> import numpy as np
>>> a = np.arange(15).reshape(3, 5)
>>> a
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
>>> a.shape
(3, 5)
>>> a.ndim
2
>>> a.dtype.name
'int64'
>>> a.itemsize
8
>>> a.size
15
>>> type(a)
<type 'numpy.ndarray'>
>>> b = np.array([6, 7, 8])
>>> b
array([6, 7, 8])
>>> type(b)
<type 'numpy.ndarray'>
```
