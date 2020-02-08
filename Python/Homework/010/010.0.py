#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 20:57
# User    : Magic
# Product : PyCharm
# Project : 010
# File    : 010.0.py
# Intro   : No Description


member = ['小甲鱼', '黑夜', '迷途', '怡静', '秋舞斜阳']

for each in range(1,10,2):
    p = int(input("请输入："))
    member.insert(each,p)

print(member)