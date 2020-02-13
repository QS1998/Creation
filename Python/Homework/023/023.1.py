#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/10 14:33
# User    : Magic
# Product : PyCharm
# Project : 023
# File    : 023.1.py
# Intro   : No Description
result1 = []


def get_digits(n):
    if n:
        result1.append(n % 10)
        get_digits(n // 10)


get_digits(12345)
print(result1)


def dec2bin(dec):
    result2 = ''

    if dec:
        result2 = dec2bin(dec // 2)
        return result2 + str(dec % 2)
    else:
        return result2


print(dec2bin(62))
