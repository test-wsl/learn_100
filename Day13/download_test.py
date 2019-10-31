#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from time import sleep, time


def download_task(filename):
    print('开始下载{}...'.format(filename))
    time_to_download = randint(5, 10)
    sleep(time_to_download)
    print('{}下载完成！ 耗费了{}秒'.format(filename, time_to_download))


def main():
    start = time()
    download_task('Python从入门.pdf')
    download_task('Peking.avi')
    end = time()
    print('总共耗费了{:.2f}秒'.format(end - start))


if __name__ == '__main__':
    main()
