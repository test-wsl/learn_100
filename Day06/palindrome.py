#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_pal(num):
    tem = num
    total = 0
    while tem > 0:
        if tem % 10 ==0:
            total = 0
            break
        else:
            total = total * 10 + tem % 10
            tem //= 10
    return total == num


def print_pal(num):
    i = 1
    sum = 0
    while sum < num:
        if is_pal(i):
            print (i)
            sum += 1
        i += 1



if __name__ == '__main__':
    num = int(input("输入要输出的回文数的个数"))
    print_pal(num)