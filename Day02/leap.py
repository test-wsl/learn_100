#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_leap(year):
    return (year % 4 == 0 and year % 100 !=0 or year % 400 == 0)

if __name__ == '__main__':
    year = int(input("输入年份"))
    print (is_leap(year))
