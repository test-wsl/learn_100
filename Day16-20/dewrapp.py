#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import time
from functools import wraps


def record_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        print(f'{func.__name__}: {time() - start}秒')

    return wrapper
