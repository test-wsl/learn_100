#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fibo(n):
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


if __name__ == '__main__':
    n = int(input("输入数列个数"))
    for i in range(1, n+1):
        print (fibo(i))

