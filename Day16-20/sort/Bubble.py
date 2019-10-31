#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def bubble_sort(origin_items, comp=lambda x, y: x > y):
    items = origin_items
    for i in range(len(items) - 1):
        swapped = False
        for j in range(i, len(items) - 1 - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(len(items) - 2 - i, i, -1):
                if comp(items[j - 1], items[j]):
                    items[j], items[j - 1] = items[j - 1], items[j]
                    swapped = True
        if not swapped:
            break
    return items


def bubble_sort2(origin_items, comp=lambda x, y: x > y):
    items = origin_items
    for i in range(len(items) - 1):
        for j in range(len(items) - i - 1):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
    return items


def main():
    num = []
    for i in range(10):
        num.append(random.randint(0, 100))
    print("原始序列为：", num)
    print("排序之后为：", bubble_sort(num))
    print("2排序之后为:", bubble_sort2(num))


if __name__ == '__main__':
    main()
