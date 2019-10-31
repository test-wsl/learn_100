#!/usr/bin/env python
# -*- coding: utf-8 -*-
from threading import Thread

import requests


class DownloadHanlder(Thread):

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        filename = self.url[self.url.rfind('/') + 1:]
        resp = requests.get(self.url)
        with open(r'D:\python\file\learn\test\\' + filename, 'wb') as f:
            f.write(resp.content)


def main():
    # 通过requests获取网络资源
    # 首拍卖行接口提供的网络API
    resp = requests.get(
        'http://api.tianapi.com/meinv/?key=d750d08c4932acf5c5e4f8cb4f901597&num=5'
    )
    data = resp.json()
    for mm_dict in data['newslist']:
        url = mm_dict['picUrl']
        DownloadHanlder(url).start()


if __name__ == '__main__':
    main()
