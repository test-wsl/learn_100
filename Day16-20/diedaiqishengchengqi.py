#!/usr/bin/env python
# -*- coding: utf-8 -*-


def fib(num):
    """生成器"""
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
        yield a


class Fib(object):
    """迭代器"""

    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()


def main():
    for i in fib(40):
        print(i, end='\t' * 3)
    fib1 = Fib(50)
    for i in fib1:
        print(i)


if __name__ == '__main__':
    main()
