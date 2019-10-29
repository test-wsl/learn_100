#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math

num = int(input("请输入正整数： "))

end = int(math.sqrt(num))

is_Prime = True

for x in (2, end + 1):
    if num % x == 0:
        is_Prime = False
        break
if is_Prime and num != 1:
    print ("{}是素数".format(num))
else:
    print ("{}不是素数".format(num))
