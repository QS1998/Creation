#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/13 6:54
# User    : Magic
# Product : PyCharm
# Project : 029
# File    : 029.1.py
# Intro   : No Description


first_file_name = 'something.txt'  # input("请输入需要比较的头一个文件名:")
second_file_name = 'something2.txt'  # input("请输入需要比较的另一个文件名:")

try:
    with open('%s' % first_file_name, 'r') as first_file:
        with open('%s' % second_file_name, 'r') as second_file:
            content1 = first_file.readlines()
            content2 = second_file.readlines()
            diff_elem_set = set(content1).symmetric_difference(content2)
            for each_elem in diff_elem_set:
                if each_elem in content1:
                    index1 = content1.index(each_elem)
                    print("第一个文件中第 %d 行:%s"
                          "第二个文件中第 %d 行:%s" % (index1 + 1, each_elem, index1 + 1, content2[index1]))
                else:
                    index2 = content2.index(each_elem)
                    print("第一个文件中第 %d 行:%s"
                          "第二个文件中第 %d 行:%s" % (index2 + 1, content1[index2], index2 + 1, each_elem))
except OSError as reason:
    print("出错啦:" + str(reason))
