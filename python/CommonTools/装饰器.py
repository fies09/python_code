#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2024/11/6 18:16
# @Author     : fany
# @Project    : PyCharm
# @File       : 装饰器.py
# @Description:
def log_it(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_it
def do_something():
    print("I'm doing something...")

do_something()
