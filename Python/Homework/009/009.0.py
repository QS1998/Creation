#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 18:31
# User    : Magic
# Product : PyCharm
# Project : 009
# File    : 009.0.py
# Intro   : 验证用户密码程序


password = "小甲鱼是帅哥"
times = 3  # 一共提供3+1=4次机会

while times:
    temp = input("请输入密码：")
    if temp == password:
        print("密码正确，进入程序...")
        break
    elif '*' in temp:  # 当输入的密码中含有*号时提示重新输入
        print("密码中不能含有'*'号！您还有%d次机会！" % times, end="")
        continue
    else:  # 每次输错密码剩余次数便减一
        print("密码输入错误！您还有%d次机会！" % (times-1))
    times -= 1