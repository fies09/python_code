#!/usr/bin/env python
# -*- coding = utf-8 -*-
# @Time       : 2023/2/13 00:53
# @Author     : fany
# @Project    : PyCharm
# @File       : 02_获取指定目录下的所有文件.py
# @description:
import os

def find_file(search_path, include_str=None, filter_strs=None):
    """
    查找指定目录下所有的文件（不包含以__开头和结尾的文件）或指定格式的文件，若不同目录存在相同文件名，只返回第1个文件的路径
    :param search_path: 查找的目录路径
    :param include_str: 获取包含字符串的名称
    :param filter_strs: 过滤包含字符串的名称
    """
    if filter_strs is None:
        filter_strs = []

    files = []
    # 获取路径下所有文件
    names = os.listdir(search_path)
    for name in names:
        path = os.path.abspath(os.path.join(search_path, name))
        if os.path.isfile(path):
            # 如果不包含指定字符串则
            if include_str is not None and include_str not in name:
                continue

            # 如果未break，说明不包含filter_strs中的字符
            for filter_str in filter_strs:
                if filter_str in name:
                    break
            else:
                files.append(path)
        else:
            files += find_file(path, include_str=include_str, filter_strs=filter_strs)
    return files


if __name__ == '__main__':
    # 获取全部文件
    f = find_file("./test")
    print(f)

    # 获取包含指定字符的文件
    f = find_file("./test", include_str=".py")
    print(f)

    # 获取不包含指定字符的文件
    f = find_file("./test", filter_strs=[".pyc", "__init__"])
    print(f)

    # 获取包含指定字符且不包含某些指定字符的文件
    f = find_file("./test", include_str=".py", filter_strs=[".pyc", "__init__"])
    print(f)
