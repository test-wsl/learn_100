#!/usr/bin/env python
# -*- coding: utf-8 -*-


def gcd(x, y):
    x, y = (y, x) if x > y else (x, y)
    for factor in range(x, 0, -1):
        if x % factor == 0 and y % factor ==0:
            return factor

def lcm(x, y):
    return x * y // gcd(x, y)

if __name__ == '__main__':
    x = int(input("x = "))
    y = int(input("y = "))

    print ("最大公约数为 ： ", gcd(x, y))
    print ("最小公倍数为 ： ", lcm(x, y))
