#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/3 21:49
# User    : Magic
# Product : PyCharm
# Project : 017
# File    : 017.0.py
# Intro   : 快速幂算法求末三位数字
import math


def fastpower(base, power):
    result = 1
    while power > 0:
        if power & 1:  # 此处等价于if power % 2 == 1
            result = result * base
        power >>= 1  # 此处等价于power = power / 2
        base *= base
    return result


def fastpower_mod1000(base, power):
    result = 1
    while power > 0:
        if power & 1:  # 此处等价于if power % 2 == 1
            result = result * base % 1000
        power >>= 1  # 此处等价于power = power / 2
        base = (base * base) % 1000
    return result


def built_in_power(x, y):
    answer = x ** y
    return answer


mod1000 = fastpower_mod1000(9, 1234567)
result1 = fastpower(9, 1234567)
result2 = built_in_power(9, 1234567)