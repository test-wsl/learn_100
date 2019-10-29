#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
百钱白鸡


version: 0.1
"""

for x in range(0,20):
    for y in range(0,33):
        z = 92 - x -y
        if 5 * x + y * 3 + z * 1 == 100:
            print ('公鸡：{}只，母鸡 : {}只，小鸡：{}只'.format(x,y,z))
