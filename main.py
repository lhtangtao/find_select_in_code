#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=find_select_in_code
#author=lhtangtao
#time=2018/5/14 20:03
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=添加描述信息
"""
from file import get_all_file, find_keyword_in_file
from folder import get_folder_useful


def final(kind, path, keyword):
    file_list = []
    folder_list = []
    folder = get_folder_useful(path)  # 获取所有的有用文件夹 返回一个列表
    for i in folder:
        folder_list.append(i)
    for i in folder_list:
        folder_file = get_all_file(i, kind)  # 文件夹里的文件
        for i in folder_file:
            file_list.append(i)
    for i in file_list:
        find_keyword_in_file(i, keyword)


if __name__ == '__main__':
    final(".java", "/Users/taotang/GitOfGeely/judger/", "select")
