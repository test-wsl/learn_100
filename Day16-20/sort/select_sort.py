#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def select_sort(origin_items, comp=lambda x, y: x < y):
    items = origin_items[:]
    for i in range(len(items) - 1):
        min_index = i
        for j in range(i + 1, len(items)):
            if comp(items[j], items[min_index]):
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]
    return items


def main():
    item = []
    for i in range(5):
        item.append(random.randint(1, 100))
    print("原始序列为:", item)
    print("排序之后为:", select_sort(item))


if __name__ == '__main__':
    main()
