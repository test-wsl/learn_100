#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def get_suffix(filename, has_dot=False):
    """
    获取文件后缀名

    :param filename: 文件名
    :param has_dot: 返回后缀是否需要带点,默认为不需要

    :return: 文件后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''


def main():
    files = os.listdir(r'D:\python\file\learn\Day07')
    for f in files:
        print('{}的后缀为{}'.format(f, get_suffix(f)))


if __name__ == '__main__':
    main()
