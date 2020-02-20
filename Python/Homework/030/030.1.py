#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/18 12:49
# User    : Magic
# Product : PyCharm
# Project : 030
# File    : 030.1.py
# Intro   : 编写一个程序，计算当前文件夹下所有文件的大小
import os  # 引入os模块


def file_size_count(this_dir):
    """定义一个文件大小计算函数"""

    os.chdir(this_dir)  # 切换工作目录
    file_name_list = os.listdir(this_dir)  # 将当前工作目录下的内容转换为列表存储在file_name_list中
    for i in file_name_list:  # 遍历列表用os.path.getsize()方法计算每个文件大小并按照指定格式打印
        print("{0}  【{1:0.2f}KB】".format(i, os.path.getsize(i) / 1024))


def path_trans(raw_path):
    """定义一个路径字符串转换函数，用于将当前操作系统中的路径字符串转换成标准路径"""

    path_list = raw_path.split('\\')  # 将传入的原始路径字符串以\为标志切割并保存在列表path_list中
    standard_path = os.sep.join(path_list)  # 再将os.sep插入到每个元素之间并将其重新拼接成标准字符串
    return standard_path


actual_dir = path_trans(input("请输入需要查询的目录:"))
file_size_count(actual_dir)