#!/usr/bin/env python
# -*- coding: utf-8 -*-
import itertools

for i in itertools.permutations('ABCD'):
    print(i)

print('#' * 20)
for i in itertools.combinations('ABCDE', 4):
    print(i)

print('#' * 20)
for i in itertools.product('ABCD', '123'):
    print(i)
