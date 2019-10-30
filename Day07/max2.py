#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def max2(x):
    """
    找到一个列表中最大的两个值

    :param x: 列表

    :return m1, m2: 最大的值和第二大的值
    """
    m1, m2 = (x[0], x[1]) if x[0] > x[1] else (x[1], x[0])
    for index in range(2, len(x)):
        if x[index] > m1:
            m2 = m1
            m1 = x[index]
        elif x[index] > m2:
            m2 = x[index]
    return m1, m2


def main():
    num = []
    for i in range(20):
        num.append(random.randint(0, 100))
    print("{}中最大的两个为{}".format(num, max2(num)))


if __name__ == '__main__':
    main()
