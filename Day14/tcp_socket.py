#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
from socket import socket, SOCK_STREAM, AF_INET


def main():
    # 1,创建套接字对象并制定传输服务
    # family = AF_INET  - IPV4
    # family = AF_INTE6  - IPV6
    # type = SOCK_STREAM  - TCP
    # type = SOCK_DGRAM  - UDP
    # type = SOCK_RAW  - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2. 绑定IP好端口（端口区分服务）
    # 同一时间在同一端口只能绑定一个服务
    server.bind(('192.168.1.165', 9898))
    # 3. 监听- 监听客户端连接到服务器
    # 参数 512 为连接队列大小
    server.listen(512)
    print('服务器开始监听')
    while True:
        # 4. 通过循环接受客户端连接并做处理
        # accept 是一个阻塞方法如果连接到服务器代码不会向下执行
        # accept 返回一个元祖， 第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址
        client, addr = server.accept()
        print(str(addr) + '连接到服务器')
        # 5. 发送数据
        client.send((str(datetime.now()).encode('utf-8')))
        # 6. 断开连接
        client.close()


if __name__ == '__main__':
    main()
