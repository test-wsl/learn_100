#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(num, temp={}):
    """递归方式计算"""
    if num in (1, 2):
        return 1
    try:
        return temp[num]
    except KeyError:
        temp[num] = fib(num - 1) + fib(num - 2)
        return temp[num]


if __name__ == '__main__':
    tmp = {}
    n = 100
    for i in range(1, 100):
        print(fib(i, tmp))
