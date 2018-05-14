#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
#name=find_select_in_code 
#author=lhtangtao
#time=2018/5/14 14:31
#Mail=tangtao@lhtangtao.com
#git=lhtangtao
#my_website=http://www.lhtangtao.com
#Description=对文件夹的一些操作
"""
import os


def get_all_folder(path):
    """
    输入一个路径获取里面的所有文件夹信息  返回一个列表
    :param path:
    :return:
    """
    folder_list = []
    for root, dirs, files in os.walk(path):
        if "." not in root:  # 去除idea和git的文件夹
            folder_list.append(root)
    return folder_list


def select_folder(path):
    """
    输入路径，筛选出这个文件夹下方是不是有文件，如果有则返回true 没有就返回false
    :param path:
    :return:
    """
    file_list = os.listdir(path)
    for i in file_list:
        if i != "." or i != "..":
            if not os.path.isdir(path + "/" + i):
                return True
    return False


def get_folder_useful(path):
    """
    获取真实可用的路径列表
    :param path:
    :return:
    """
    useful_list = []
    path_list = get_all_folder(path)
    for i in path_list:
        if select_folder(i):
            useful_list.append(i)
    return useful_list


if __name__ == '__main__':
    print get_folder_useful("/Users/taotang/GitOfGeely/judger/judger-api")
