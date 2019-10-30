#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import time


def generate_code(code_len=4):
    """
    生成指定长度的验证码

    :param code_len: 验证码长度（默认为四位）

    :return: 大小写英文及数字组成的随机验证码
    """
    all_chars = '0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    last_pos = len(all_chars) - 1
    code = ''
    for i in range(code_len):
        index = random.randint(0, last_pos)
        code += all_chars[index]
    return code


def main():
    print("验证码为：{}".format(generate_code(10)))


if __name__ == '__main__':
    while True:
        main()
        time.sleep(1)
