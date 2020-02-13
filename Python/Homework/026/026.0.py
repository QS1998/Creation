#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/11 14:53
# User    : Magic
# Product : PyCharm
# Project : 026
# File    : 026.0.py
# Intro   : 登录小程序

data_base = {}  # 创建一个空字典用于存放用户名及密码

while True:  # 程序在线运行
    print("""
|--- 新建用户:N/n ---|
|--- 登录账号:E/e ---|
|--- 退出程序:Q/q ---|""")
    order = input("|--- 请输入指令代码:")

    # 当用户输入N或n时，执行注册功能
    if order in 'Nn':
        chance = 5  # 限制5次失败机会
        while chance:
            user_name = input("请输入用户名:")
            if user_name in data_base:
                print("该用户名已经被使用，请重新输入！")
                chance -= 1
                continue
            else:
                user_password = input("请输入密码:")
                data_base[user_name] = user_password
                print("注册成功，赶紧试试登录吧^_^")
                break
        # 当5次机会都创建失败时，自动返回到开始页面
        else:
            print("\n操作过于频繁！\n"
                  "程序已自动返回初始页面！")
            continue

    # 当用户输入E或e时，执行登录功能
    elif order in 'Ee':
        chance = 3  # 限制3次失败机会
        while chance:
            user_name = input("请输入用户名:")
            user_password = input("请输入密码:")

            # 当用户名或密码其中只要有一个输入错误时，告知用户重新输入，并减少一次失败机会
            if user_name not in data_base:
                print("用户名或密码错误！请重新输入！")
                chance -= 1
                continue
            elif user_password != data_base.get(user_name):
                print("用户名或密码错误！请重新输入！")
                chance -= 1
                continue
            # 当用户名和密码均输入正确时，进入欢迎页面
            else:
                print("欢迎进入xxoo系统！")
                break
        # 当用户三次机会都用光时，自动返回初始页面
        else:
            print("您已经三次输入错误！\n"
                  "程序已自动返回初始页面！")
            continue
        break  # 当登录成功时退出程序

    # 当用户输入Q或q时，退出程序
    elif order in 'Qq':
        print("\n正在退出登录程序...\n"
              "感谢使用，再见！")
        break

    # 当用户输入的指令不是默认指令中的任一项时，提示用户重新输入
    else:
        print("指令输入错误！请重新输入！")
        continue

    continue  # 注册成功后返回初始页面
