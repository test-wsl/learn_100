#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math


def circle_per(radius):
    return 2 * math.pi * radius


def circle_area(radious):
    return math.pi * radious * radious


if __name__ == '__main__':
    r = float(input("输入圆的半径"))
    print("周长： {:.2f}".format(circle_per(r)))
    print("面积：{:.2f}".format(circle_area(r)))
