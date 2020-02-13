#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/10 10:15
# User    : Magic
# Product : PyCharm
# Project : 023
# File    : 023.0.py
# Intro   : No Description


def dec2bin(dec):
    """递归法将十进制数字转换为二进制数字"""

    result = ''
    if dec:
        result = dec2bin(dec // 2)
        return result + str(dec % 2)
    else:
        return result


temp = int(input("请输入一个十进制数:"))
print(dec2bin(temp))
