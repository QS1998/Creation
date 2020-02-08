#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/3 21:25
# User    : Magic
# Product : PyCharm
# Project : 016
# File    : 016.1.py
# Intro   : No Description


def sum_fx(x):
    result = 0

    for each in x:
        if (type(each) == int) or (type(each) == float):
            result += each
        else:
            continue

    return result


print(sum_fx([1, 2.1, 2.3, 'a', '1', True]))
