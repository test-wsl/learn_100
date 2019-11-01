#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def merge_sort(items, comp=lambda x, y: x <= y):
    """
    归并排序
    :param items:
    :param comp:
    :return:
    """
    if len(items) < 2:
        return items[:]
    mid = len(items) // 2
    left = merge_sort(items[:mid], comp)
    right = merge_sort(items[mid:], comp)
    return merge(left, right, comp)


def merge(items1, items2, comp):
    """合并"""
    items = []
    index1, index2 = 0, 0
    while index1 < len(items1) and index2 < len(items2):
        if comp(items1[index1], items2[index2]):
            items.append(items1[index1])
            index1 += 1
        else:
            items.append(items2[index2])
            index2 += 1
    items += items1[index1:]
    items += items2[index2:]
    return items


def main():
    num = []
    for i in range(10):
        num.append(random.randint(0, 100))
    print("原始序列为:", num)
    print("排序之后：", merge_sort(num))


if __name__ == '__main__':
    main()
