#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/14 11:33
# User    : Magic
# Product : PyCharm
# Project : 030
# File    : 030.0.py
# Intro   : 编写一个程序，统计当前目录下每个文件类型的文件数
import os  # 引入os模块


def count_file(this_dir):
    """定义一个文件类型计数函数"""

    type_dict = {}  # 创建一个空字典，用于存储文件类型及该类型个数
    file_name_list = os.listdir(this_dir)  # 用os命令将this_dir中的文件及文件夹打包成列表返回给file_name_list

    for i in file_name_list:  # 遍历文件名列表
        f_name, f_extension = os.path.splitext(i)  # 用os.path中的splitext方法分离文件名及其拓展名并分别赋值给f_name和f_extension
        if f_extension == '':  # 如果文件无扩展名，则将其类型定义为文件夹
            f_extension = '文件夹'

        # 用get方法访问字典type_dict中是否已存在f_extension这个键，若不存在，则创建一个名为f_extension的键并将其赋值为1
        if type_dict.get(f_extension) is None:
            type_dict[f_extension] = 1
        else:  # 若已存在，则将其对应的值+1
            type_dict[f_extension] += 1

    # 遍历字典中的项并将其按照指定格式打印出来
    for j in type_dict.items():
        print("该文件夹下共有类型为【{0}】的文件{1}个".format(j[0], j[1]))


actual_dir = input("请输入需要查询的文件目录:")
count_file(actual_dir)