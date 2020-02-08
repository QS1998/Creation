#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 19:49
# User    : Magic
# Product : PyCharm
# Project : 009
# File    : 009.1.py
# Intro   : 求100~999之间的水仙花数


print("100~999之间的水仙花数如下所示：")
for each in range(100, 1000):
    a = each // 100  # 求百位数字
    b = each // 10 % 10  # 求十位数字
    c = each % 10  # 求个位数字
    if each == (a ** 3) + (b ** 3) + (c ** 3):
        print(each)  # 将找到的水仙花数打印出来
