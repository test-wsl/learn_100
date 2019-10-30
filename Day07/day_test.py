#!/usr/bin/env python
# -*- coding: utf-8 -*-


def is_leap_year(year):
    """
    判断指定年份是否为闰年

    :param year: 年份
    :return: 闰年返回True，平年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def which_day(year, month, date):
    """
    计算传入的日期为这一年的第几天

    :param year: 年
    :param moth: 月
    :param date: 日
    :return: 第几天
    """
    days_of_month = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for index in range(month - 1):
        total += days_of_month[index]
    return total + date


def main():
    print(which_day(1980, 12, 9))
    print(which_day(1982, 12, 31))
    print(which_day(2019, 1, 1))
    print(which_day(2000, 3, 1))


if __name__ == '__main__':
    main()
