#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
from threading import Lock

import locker as locker


def singleton(cls):
    """
    装饰类的装饰器
    :param cls:
    :return:
    """
    instances = {}
    locker = Lock()

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            with locker:
                if cls not in instances:
                    instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class President():
    """总理（单例）"""
    pass
