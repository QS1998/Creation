#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/1/31 18:58
# User    : Magic
# Product : PyCharm
# Project : 005
# File    : 005.1.py
# Intro   : <输入给定年份，判断是否为闰年>

while 1:
    print("请输入年份：", end="")
    temp = input()

    while not temp.isdigit():
        if temp == 'Exit':
            break
        print("输入错误！\n"
              "请重新输入年份：", end="")
        temp = input()

    if temp == 'Exit':
        break

    year = int(temp)

    if not year % 400:
        print("%d年是闰年！" % year)
    elif not year % 4:
        if not year % 100:
            print("%d年不是闰年！" % year)
        else:
            print("%d年是闰年！" % year)
    else:
        print("%d年不是闰年！" % year)

print("已成功退出<闰年判断>程序。")