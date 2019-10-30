#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time


def main(cont):
    while True:
        # 清空屏幕输出
        os.system('cls')
        print(cont)
        # 休眠200ms
        time.sleep(2)
        cont = cont[1:] + cont[0]


if __name__ == '__main__':
    cont = input("输入要展示的内容")
    main(cont)
