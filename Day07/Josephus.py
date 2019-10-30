#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
约瑟夫环
15个基督徒和15个非基督徒遇险，由1到9报数，扔到9就扔出，直到扔15个
"""


def main():
    persion = [True] * 30
    counter, index, number = 0, 0, 0
    while counter < 15:
        if persion[index]:
            number += 1
            if number == 9:
                persion[index] = False
                counter += 1
                number = 0
        index += 1
        index %= 30

    for index, per in enumerate(persion):
        print('基' if per else '非', end=' ')


if __name__ == '__main__':
    main()
