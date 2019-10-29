#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
将华氏温度转为摄氏温度

version: 0.1
"""


def f2c(f):
    """华氏转摄氏公式为 C = (F-32) \ 1.8"""
    c = (f - 32) / 1.8
    return c


if __name__ == '__main__':
    f = float(input("输入华氏温度:"))
    c = f2c(f)
    print ('{0:.1f}华氏度 = {1:.1f}摄氏度'.format(f, c))
