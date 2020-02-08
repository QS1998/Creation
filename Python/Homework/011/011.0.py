#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/2 6:35
# User    : Magic
# Product : PyCharm
# Project : 011
# File    : 011.0.py
# Intro   : No Description


list1 = [(x, y) for x in range(10) for y in range(10) if x%2==0 if y%2!= 0]
list2 = []
for x in range(10):
    for y in range(10):
        if x%2==0:
            if y%2!=0:
                list2.append((x, y))

print(list1)
print(list2)
