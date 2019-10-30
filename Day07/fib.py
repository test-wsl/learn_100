#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        yield a


def main():
    n = int(input("输入数组个数"))
    for val in fib(n):
        print(val)


if __name__ == '__main__':
    main()
