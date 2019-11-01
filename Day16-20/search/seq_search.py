#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def seq_search(items, key):
    """
    顺序查找
    :param items:
    :param key:
    :return:
    """
    for index, item in enumerate(items):
        if item == key:
            return index
    return -1


def main():
    item = []
    for i in range(10):
        item.append(random.randint(0, 20))
    print("原始序列为 ", item)
    print('查找到的为 ', seq_search(item, 10))


if __name__ == '__main__':
    main()
