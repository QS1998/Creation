#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/3 16:04
# User    : Magic
# Product : PyCharm
# Project : 016
# File    : 016.0.py
# Intro   : 猜想内置函数min()的构造


def min_fx(x):
    least = x[0]

    for each in x:
        if each < least:
            least = each

    return least


print(min_fx('123456789'))
