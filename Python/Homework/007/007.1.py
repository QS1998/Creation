#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 12:15
# User    : Magic
# Product : PyCharm
# Project : 007
# File    : 007.1.py
# Intro   : No Description

# x, y, z = 6, 5, 4
# if x < y:
#     small = x
#     if z < small:
#         small = z
# elif y < z:
#     small = y
# else:
#     small = z

x, y, z = 6, 5, 4
small = x if x <= y else y if y <= z else z
print(small)