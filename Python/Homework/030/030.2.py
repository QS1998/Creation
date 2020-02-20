#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/18 13:36
# User    : Magic
# Product : PyCharm
# Project : 030
# File    : 030.2.py
# Intro   : No Description
import os  # 引入os模块


def file_search(init_dir, aim_file):
    """定义一个搜索函数"""

    flag = 1  # 定义一个标签，用于判断是否找到文件
    for i in os.walk(init_dir):  # 用os模块中的walk方法遍历初始文件夹并寻找目标文件
        if aim_file in i[1] or aim_file in i[2]:  # 如果目标文件或文件夹在由walk方法返回的三元组i的后两项中
            flag = 0  # 则将flag赋值为0
            print("{0}""\\{1}".format(i[0], aim_file))  # 并打印目标文件或文件夹的路径，即三元组i的第一项i[0]
    else:  # 循环正常结束
        if flag:  # 如果flag的值未改变，即未找到目标文件或文件夹，则打印以下内容
            print("目标文件'{0}'未找到!".format(aim_file))


actual_dir = input("请输入待查找的初始目录:")
actual_file = input("请输入需要查找的目标文件:")

file_search(actual_dir, actual_file)
