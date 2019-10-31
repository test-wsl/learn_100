#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json

import requests


def main():
    resp = requests.get('http://api.tianapi.com/topnews/?key=APIKey&num=15')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'], news['url'])


if __name__ == '__main__':
    main()
