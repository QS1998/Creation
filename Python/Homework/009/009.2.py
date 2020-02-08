#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 20:02
# User    : Magic
# Product : PyCharm
# Project : 009
# File    : 009.2.py
# Intro   : 三色球问题
"""
有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。
先将这 12 个球混合放在一个盒子中，从中任意摸出 8 个球，编程计算摸出
球的各种颜色搭配。
"""


Collocation = 0
print("红球    黄球    绿球")
for g in range(2, 7):
    for y in range(0, 4):
        for r in range(0, 4):
            if r + y + g == 8:
                print(' ', r, '    ', y, '    ', g)
                Collocation += 1

print("\n共计%d种颜色搭配" % Collocation)