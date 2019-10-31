#!/usr/bin/env python
# -*- coding: utf-8 -*-


def main():
    try:
        with open('guido.jpg', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('吉多.jpg', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print("无法打开指定文件")
    except IOError as e:
        print("读写文件出错")
    print("程序执行结束")


if __name__ == '__main__':
    main()
