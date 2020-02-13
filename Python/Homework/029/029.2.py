#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/13 15:35
# User    : Magic
# Product : PyCharm
# Project : 029
# File    : 029.2.py
# Intro   : 2. 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上


def display_first_lines(name, number):
    with open(name, 'r') as f:
        content = f.readlines()
        for i in content[:number]:
            print(i, end='')


file_name = input("请输入要打开的文件(例如：C:\\test.txt):")
first_lines = int(input("请输入需要显示该文件前几行:"))

display_first_lines(file_name, first_lines)
