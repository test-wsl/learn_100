#!/usr/bin/env python
# -*- coding: utf-8 -*-


<<<<<<< HEAD
def Is_leap(year):
    if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


if __name__ == '__main__':
    year = int(input("请输入年份"))
    print (Is_leap(year))
=======
def is_leap(year):
    return (year % 4 == 0 and year % 100 !=0 or year % 400 == 0)

if __name__ == '__main__':
    year = int(input("输入年份"))
    print (is_leap(year))
>>>>>>> 8abc950... Day 2
