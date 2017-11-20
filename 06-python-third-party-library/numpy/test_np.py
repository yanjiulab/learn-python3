#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import *

def test_img():

    img = lena()
    print(img)

    imshow(img,
           # 设置坐标范围
           extent=[-25, 25, -25, 25],
           # 设置colormap
           cmap=cm.bone)
    colorbar()

def test_basic(a):
    a = np.arange(15).reshape(3, 5)
    print(a)
    print(a.data)
    print(a.ndim)
    print(a.shape)
    print(a.dtype.name)
    print(a.itemsize)
    print(a.size)
    print(type(a))

if __name__ == '__main__':
    test_img()
