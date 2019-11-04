#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
from concurrent.futures.thread import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def deposit(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, account, money):
        self.account = account
        self.money = money
        # 自定义线程的初始化必须调用父类的初始化方法
        super().__init__()

    def run(self):
        self.account.deposit(self.money)


def main():
    account = Account()
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for i in range(100):
        # threading.Thread(
        #     target=account.deposit, args=(1, )
        # ).start()
        AddMoneyThread(account, 1).start()
    pool.shutdown()
    for future in futures:
        future.result()
    print(account.balance)


if __name__ == '__main__':
    main()
