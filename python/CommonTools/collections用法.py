#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2024/11/6 18:36
# @Author     : fany
# @Project    : PyCharm
# @File       : collections用法.py
# @Description:
# from collections import defaultdict
#
# my_dict = defaultdict(int)
# my_dict['a'] += 1
# print(my_dict['a'])  # 输出 1

from collections import Counter

words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = Counter(words)
print(word_count)
