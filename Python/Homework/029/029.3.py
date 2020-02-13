#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/13 17:30
# User    : Magic
# Product : PyCharm
# Project : 029
# File    : 029.3.py
# Intro   :
"""呃，不得不说我们的用户变得越来越刁钻了。要求在上一题的基础上扩展，用户可以随意输入需要显示的行数。
（如输入13:21打印第13行到第21行，输入:21打印前21行，输入21:则打印从第21行开始到文件结尾所有内容）
"""


def display_first_lines(name, starts, ends):
    with open(name, 'r', encoding='utf-8') as f:
        content = f.readlines()

        if starts == '' and ends != '':
            ends = int(ends)
            print("文件%s从开始到第%d行的内容如下:\n\n\n" % (name, ends))
            for i in content[:ends]:
                print(i, end='')
        elif starts != '' and ends == '':
            starts = int(starts)
            print("文件%s从第%d行到末尾的内容如下:\n\n\n" % (name, starts))
            for i in content[starts:]:
                print(i, end='')
        elif starts != '' and ends != '':
            starts = int(starts)
            ends = int(ends)
            print("文件%s从第%d行到第%d行的内容如下:\n\n\n" % (name, starts, ends))
            for i in content[starts:ends]:
                print(i, end='')
        else:
            print("文件%s的全文内容如下:\n\n\n" % name)
            for i in content[:]:
                print(i, end='')

        print("\n" * 7, end='')


while True:
    file_name = input("请输入要打开的文件(例如：C:\\test.txt):")
    [start_line, end_line] = input("请输入需要显示的行数【格式如 13:21 或 :21 或 21:】").split(':')
    display_first_lines(file_name, start_line, end_line)
