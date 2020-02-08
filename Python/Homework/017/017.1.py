#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/3 22:06
# User    : Magic
# Product : PyCharm
# Project : 017
# File    : 017.1.py
# Intro   : 辗转相除法求两正整数的最大公约数


def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b


while 1:
    x, y = input("请输入两个整数：").split(',')
    X, Y = int(x), int(y)
    print("%d与%d的最大公约数为:%d" % (X, Y, gcd(X, Y)))
