#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/5 21:39
# User    : Magic
# Product : PyCharm
# Project : 019
# File    : 019.0.py
# Intro   : No Description


def judge_palindrome(string_in):
    """判断一句话是否为回文联"""

    list0 = list(string_in)
    list1 = list0[::-1]
    if list1 == list0:
        print("是回文联！")
    else:
        print("不是回文联！")


temp = input("请输入一句话：")
judge_palindrome(temp)
