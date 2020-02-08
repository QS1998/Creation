#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/1/31 21:49
# User    : Magic
# Product : PyCharm
# Project : 006
# File    : 006.2.py
# Intro   : No Description

for i in range(7,10001,7):
    if (i % 2 == 1) and (i % 3 == 2) and (i % 5 == 4) and (i % 6 == 5):
        print(i)
