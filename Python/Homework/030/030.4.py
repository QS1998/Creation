#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/18 16:41
# User    : Magic
# Product : PyCharm
# Project : 030
# File    : 030.4.py
# Intro   : 编写一个程序，用户输入关键字，查找当前文件夹内
# （如果当前文件夹内包含文件夹，则进入文件夹继续搜索）所有含有
# 该关键字的文本文件（.txt后缀），要求显示该文件所在的位置以
# 及关键字在文件中的具体位置（第几行第几个字符）
import os


def line_retrieve(line, key):
    """检索并记录一行中关键词的出现次数和具体位置"""

    line_len = len(line)
    key_len = len(key)
    column = []
    for i in range(line_len):
        if line[i:i+key_len] == key:
            column.append(i)
    return column


def exact_search(aim_dir, key_word):
    """定义一个精确搜索函数，用于查找文件内部信息"""

    os.chdir(aim_dir)
    key_location_list = []
    for cur_path, in_dir, in_file in os.walk(aim_dir):
        for each_file in in_file:
            if each_file.endswith('.txt'):
                with open(each_file, ) as f:
                    for line_number, each_line in enumerate(f.readlines()):
                        column_number = line_retrieve(each_line, key_word)
                        final_path = os.path.join(cur_path, each_file)
                        key_location_list.append([final_path, line_number, column_number])
    for path, line, column in key_location_list:
        print(f"在文件【{path}】中找到关键字【{key_word}】\n"
              f"关键字出现在第{line}行，第{column}个位置。\n")


actual_aim_dir = input("请输入目标文件夹:")
actual_key_word = input("请输入关键字:")

exact_search(actual_aim_dir, actual_key_word)
