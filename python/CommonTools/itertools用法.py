#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2024/11/6 18:40
# @Author     : fany
# @Project    : PyCharm
# @File       : itertools用法.py
# @Description: 将第二个列表中的元素依次分配给第一个列表中的元素
import itertools

colors = ["red", "blue"]
sizes = ["S", "M", "L"]
combinations = itertools.product(colors, sizes)

for combo in combinations:
    print(combo)
