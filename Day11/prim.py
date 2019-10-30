#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


def is_prime(n):
    """
    判断素数的函数
    :param n:
    :return:
    """
    assert n > 0
    for factor in range(2, int(sqrt(n) + 1)):
        if n % factor == 0:
            return False
    return True if n != 1 else False


def main():
    filenames = ('a.txt', 'b.txt', 'c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for num in range(1, 1000000):
            if is_prime(num):
                if num < 100:
                    fs_list[0].write(str(num) + '\n')
                elif num < 1000:
                    fs_list[1].write(str(num) + '\n')
                else:
                    fs_list[2].write(str(num) + '\n')
    except IOError as ex:
        print(ex)
        print('读写文件出错')
    finally:
        for fs in fs_list:
            fs.close()
    print("操作完成")


if __name__ == '__main__':
    main()
