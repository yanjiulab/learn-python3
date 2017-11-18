#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np


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

