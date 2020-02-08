#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/5 21:46
# User    : Magic
# Product : PyCharm
# Project : 019
# File    : 019.1.py
# Intro   : No Description


def cha_classify_stat(*string):
    """多字符串字符分类统计"""
    length = len(string)
    for i in range(length):
        letter = num = space = symbol = 0
        for j in string[i]:
            if 'A' <= j <= 'z':
                letter += 1
            elif '0' <= j <= '9':
                num += 1
            elif j == ' ':
                space += 1
            else:
                symbol += 1
        print("第%d个字符串共有：英文字母%d个，数字%d个，\
空格%d个，其它字符%d个。" % (i+1, letter, num, space, symbol))


raw_string = input("请输入一个或多个字符串(以TAB键隔开):")
processed_string = raw_string.split("\t")
print(processed_string)
cha_classify_stat(*processed_string)
