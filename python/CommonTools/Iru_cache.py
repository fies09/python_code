#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2024/11/6 18:37
# @Author     : fany
# @Project    : PyCharm
# @File       : Iru_cache.py
# @Description: 减少函数计算次数，缓存机制
from functools import lru_cache


@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


print(fib(50))
