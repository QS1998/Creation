#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/18 14:48
# User    : Magic
# Product : PyCharm
# Project : 030
# File    : 030.3.py
# Intro   : 编写一个程序，用户输入开始搜索的路径，
# 查找该路径下（包含子文件夹内）所有的视频格式文件
# （要求查找mp4, rmvb, avi的格式即可），并创建一
# 个文件（videoList.txt）存放所有找到的文件的路径
import os  # 引入os模块


def format_find(this_path, ext_list, target_path):
    """定义一个格式查找函数，用于查找指定目录中指定拓展名的文件并将其路径记录在一个文本文件中"""

    path_list = []
    for i in os.walk(this_path):
        for j in i[2]:
            for k in ext_list:
                if k in j:
                    path_list.append(i[0] + '\\' + j)
    else:
        path_str = '\n\n'.join(path_list)
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(path_str)
        print("保存成功!")


def path_trans(raw_path):
    """定义一个路径字符串转换函数，用于将当前操作系统中的路径字符串转换成标准路径"""

    path_list = raw_path.split('\\')  # 将传入的原始路径字符串以\为标志切割并保存在列表path_list中
    standard_path = os.sep.join(path_list)  # 再将os.sep插入到每个元素之间并将其重新拼接成标准字符串
    return standard_path


actual_this_path = path_trans(input("请输入待查找的初始目录:"))
actual_ext_list = input("请输入需要查找的拓展名[以','号间隔]:").split(',')
actual_target_path = path_trans(input("请输入需要保存的路径:"))

format_find(actual_this_path, actual_ext_list, actual_target_path)
