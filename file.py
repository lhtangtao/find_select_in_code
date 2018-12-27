#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=find_select_in_code 
#author=lhtangtao
#time=2018/5/14 14:30
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=对文件的一些操作
"""
import os


def get_all_file(folder_path):
    """
    输入文件夹地址，返回所有的文件地址列表
    :param folder_path:
    :return:
    """
    all_file = []
    all = os.listdir(folder_path)
    for i in all:
        if os.path.isfile(os.path.join(folder_path, i)):
            if i != ".DS_Store":
                i = folder_path + "/" + i
                all_file.append(i)
    return all_file


def find_keyword_in_file(file_path, keyword):
    """
    输入文件路径和关键词 把里面的
    :param file_path:
    :param keyword:
    :return:
    """
    with open(file_path) as src_file:
        for line in src_file.readlines():
            if keyword in line:
                print line

if __name__ == '__main__':
    print get_all_file("/Users/taotang/new/first")
    find_keyword_in_file("/Users/taotang//new/first/pom.xml", "elastic-job")
