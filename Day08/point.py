#!/usr/bin/env python
# -*- coding: utf-8 -*-
from math import sqrt


class Point(object):
    def __init__(self, x=0, y=0):
        """
        初始化方法

        :param x:横坐标
        :param y:纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """
        移动到指定位置

        :param x: 新的横坐标
        :param y: 新的纵坐标
        :return:
        """
        self.x = x
        self.y = y

    def move_by(self, dx=0, dy=0):
        """
        移动指定的增量
        :param dx:
        :param dy:
        :return:
        """
        self.x += dx
        self.y += dy

    def distince_to(self, other):
        """
        计算另一点距离
        :param other: 另一个点
        :return: 两点之间距离
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '({}, {})'.format(str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distince_to(p2))


if __name__ == '__main__':
    main()
