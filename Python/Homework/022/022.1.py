#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/10 9:56
# User    : Magic
# Product : PyCharm
# Project : 022
# File    : 022.1.py
# Intro   : No Description
"""1. 使用递归编写一个函数，利用欧几里得算法求最大公约数，例如 gcd(x, y) 返回值为参数 x 和参数 y 的最大公约数。"""


def gcd(x, y):
    """用递归方式实现辗转相除法"""

    if x == 0 or y == 0:
        return [x, y][x < y]
    else:
        return gcd(y, x % y)


i, j = map(int, input("请输入两个参数：").split(','))
print("参数{0}和参数{1}的最大公约数为:{2}".format(i, j, gcd(i, j)))
