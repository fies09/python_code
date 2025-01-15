#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2024/11/6 18:16
# @Author     : fany
# @Project    : PyCharm
# @File       : 生成器.py
# @Description:
def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count += 1


counter = count_up_to(5)
for num in counter:
    print(num)
