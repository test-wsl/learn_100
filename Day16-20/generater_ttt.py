#!/usr/bin/env python
# -*- coding: utf-8 -*-


price = {
    'AAPL': 191.88,
    'GOOG': 1186.96,
    'IBM': 149.24,
    'ORCL': 48.44,
    'ACN': 166.89,
    'FB': 208.09,
    'SYMC': 21.29
}

price2 = {key: value for key, value in price.items() if value > 100}
print(price2)
