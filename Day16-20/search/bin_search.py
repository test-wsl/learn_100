#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from algorithms.sort import merge_sort


def bin_search(items, key):
    """
    折半查找
    :param items:
    :param key:
    :return:
    """
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if key > items[mid]:
            start = mid + 1
        elif key < items[mid]:
            end = mid - 1
        else:
            return mid
    return -1


def main():
    num = []
    for i in range(15):
        num.append(random.randint(0, 30))
    print("原始序列为:", num)
    item = merge_sort(num)
    print("排序之后：", item)
    print("找到的序列为:", bin_search(item, 20))


if __name__ == '__main__':
    main()
