#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/12 22:25
# User    : Magic
# Product : PyCharm
# Project : 029
# File    : 029.0.py
# Intro   : No Description


file_name = input("请输入文件名:")
f = open("{0}".format(file_name), mode='a')
print("请输入文件内容【单独输入':w'保存退出】:")
while True:
    each_line = input()
    if each_line == ':w':
        break
    else:
        f.write("%s\n" % each_line)
f.close()
