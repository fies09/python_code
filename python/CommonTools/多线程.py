#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time       : 2024/11/6 18:33
# @Author     : fany
# @Project    : PyCharm
# @File       : 多线程.py
# @Description:
import threading

def crawl_site(url):
    print(f"Crawling {url}")

threads = []
for url in ["http://site1.com", "http://site2.com", "http://site3.com"]:
    t = threading.Thread(target=crawl_site, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
