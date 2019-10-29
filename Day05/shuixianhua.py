#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
寻找水仙花数

水仙花数为一个三位数，每位上的立方之和正好等于本身

version: 0.1
"""


for num in range(100, 1000):
    low = num %10
    mid = num // 10 %10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high **3:
        print (num)

