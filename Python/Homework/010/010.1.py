#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 21:07
# User    : Magic
# Product : PyCharm
# Project : 010
# File    : 010.1.py
# Intro   : No Description


member = ['小甲鱼', 88, '黑夜', 90, '迷途', 85, '怡静', 90, '秋舞斜阳', 88]

num = len(member)
for i in range(num):
    print(member[i])

for j in range(0, num, 2):
    print(member[j], ' ', member[j+1])

for k in range(0, num, 2):
    print(member[k:k+2])
