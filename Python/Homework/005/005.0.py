#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/1/31 18:55
# User    : Magic
# Product : PyCharm
# Project : 005
# File    : 005.0.py
# Intro   : No Description

import random
secret = random.randint(1,10)
guess = 0
times = 3

print("---------------我爱鱼C工作室---------------")
print("不妨猜一下小甲鱼现在心里想的是哪一个数字：", end='')

while (guess != secret) and (times > 0):
    temp = input()
    while not temp.isdigit():
        print("抱歉，输入不合法，请重新输入...")
        temp = input("不妨猜一下小甲鱼现在心里想的是哪一个数字：")
    else:
        guess = int(temp)
        times = times - 1

    if guess == secret:
        print("\n卧槽，你是小甲鱼肚子里的蛔虫吗？\n"
              "哼，猜中了也没有奖励！\n")
    else:
        if guess < secret:
            print("\n唉，小了小了~")
        else:
            print("\n唉，大了大了~")
        if times > 0:
            print("再试试吧：",end='')
        else:
            print("唔，给三次机会都猜错，不跟你玩了！")
print("--------------游戏结束，不玩辣--------------")