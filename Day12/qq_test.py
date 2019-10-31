#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求用户名有字母数字或者下划线构成，并且长度为6 - 20
qq号为5 ~ 12 的数字，首位不为0
"""
import re


def main():
    username = input("输入用户名")
    qq = input('请输入QQ号')
    # match函数的第一个参数为正则表达式字符串或者正则表达式对象
    # 第二个位匹配的字符串类型
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}', username)
    if not m1:
        print("请输入有效的用户名")
    m2 = re.match(r'^[1-9]\d{4-11}$', qq)
    if not m2:
        print("输入有效的QQ")

    if m1 and m2:
        print("输入有效")


if __name__ == '__main__':
    main()
