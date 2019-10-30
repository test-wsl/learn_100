#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random


def display(balls):
    """
    输出列表中的双色球号码
    :param balls: 选中的球
    :return:
    """
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('{:02d}'.format(ball), end=' ')
    print()


def random_select():
    """
    随机选择一组号码，红球 [] 蓝球 []
    :return:
    """
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = random.sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(random.randint(1, 16))  # 选择的蓝球
    return selected_balls


def main():
    n = int(input("投注个数"))
    for i in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
