#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep


class Clock(object):
    """
    数字时钟
    """

    def __init__(self, hour=0, minute=0, second=0):
        """
        初始化方法

        :param hour: 时
        :param minute: 分
        :param second: 秒
        """
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def run(self):
        """
        走字
        """
        self.__second += 1
        if self.__second == 60:
            self.__second = 0
            self.__minute += 1
            if self.__minute == 60:
                self.__minute = 0
                self.__hour += 1
                if self.__hour == 24:
                    self.__hour = 0

    def show(self):
        """
        显示时间
        :return: string
        """
        return '{:02d}:{:02d}:{:02d}'.format(self.__hour, self.__minute, self.__second)


def main():
    clock = Clock(23, 59, 58)
    while True:
        print(clock.show())
        sleep(1)
        clock.run()


if __name__ == '__main__':
    main()
