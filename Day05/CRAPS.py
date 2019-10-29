#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
赌博
一开始有1000元
结束为输光赌注

version: 0.1
"""
import random


money = 1000

while money > 0:
    print ("你的资产为:",money)
    needs_go_on = False
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
    first = random.randint(1, 7) + random.randint(1, 7)
    if first == 7 or first == 11:
        print ("玩家赢")
        money +=debt
    elif first == 2 or first == 3 or first == 12:
        print ("庄家赢")
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = random.randint(1, 7) + random.randint(1, 7)
        print ('玩家摇出 {}点'.format(current))
        if current == 7:
            print ("庄家赢")
            money -= debt
        elif current == first:
            print ("玩家赢")
            money += debt
        else:
            needs_go_on = True
print("破产，游戏结束")