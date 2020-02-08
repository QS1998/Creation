#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/5 18:20
# User    : Magic
# Product : PyCharm
# Project : 018
# File    : 018.2.py
# Intro   : No Description


def find_str(raw_str, sub_str):
    """2. 编写一个函数 find_str()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。
    例如：假定输入的字符串为“You cannot improve your past, but you can improve your future.
    Once time is wasted, life is wasted.”，子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。
    """
    str_length = len(raw_str)
    occur_times = 0
    for i in range(str_length - 1):
        if raw_str[i] == sub_str[0]:
            if raw_str[i + 1] == sub_str[1]:
                occur_times += 1
    else:
        return occur_times


raw_string = input("请输入目标字符串:")
sub_string = input("请输入待查找的长度为2的子字符串:")

print("子字符串'{0}'在目标字符串中共出现 {1} 次.".format(sub_string, find_str(raw_string, sub_string)))
