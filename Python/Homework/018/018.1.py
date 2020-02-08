#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/5 18:04
# User    : Magic
# Product : PyCharm
# Project : 018
# File    : 018.1.py
# Intro   : No Description


def find_daffodil_number():
    """1.寻找水仙花数
    题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
    例如153 = 1^3+5^3+3^3，因此153是一个水仙花数。编写一个程序，
    找出所有的水仙花数。
    """
    for i in range(100, 1000):
        x = i // 100
        y = (i % 100) // 10
        z = i % 10
        if i == x ** 3 + y ** 3 + z ** 3:
            print(i)


find_daffodil_number()
