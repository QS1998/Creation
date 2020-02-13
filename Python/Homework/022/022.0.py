#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/9 15:59
# User    : Magic
# Product : PyCharm
# Project : 022
# File    : 022.0.py
# Intro   : No Description
"""0. 使用递归编写一个 power() 函数模拟内建函数 pow()，即 power(x, y) 为计算并返回 x 的 y 次幂的值。"""


def power_fx(x, y):
    """用递归方法实现幂运算"""

    if y == 1:
        return x
    else:
        return x * power_fx(x, y - 1)


base = int(input("请输入底数："))
exp = int(input("请输入指数："))

print(power_fx(base, exp))
