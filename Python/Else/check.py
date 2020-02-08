#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/2 11:05
# User    : Magic
# Product : PyCharm
# Project : 013
# File    : 014.0.py
# Intro   : 密码安全性检查


# 定义一个函数，负责打印密码安全级别以及改进建议
def print_class(temp):
    print("""\
您的密码安全级别评定为：%s
请按以下方式提升您的密码安全级别：
        1.密码必须由数字、字母及特殊字符三种组合
        2.密码只能由字母开头
        3.密码长度不能低于16位\n""" % temp)


# 建立三个字符串，用于检查所输入密码中的字符是否在该三个字符串中
Letter = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
Number = "0123456789"
Symbol = r"~!@#$%^&*()_=-/,.?<>;:[]{}\|"

# 执行死循环，便于连续判断不同密码安全级别
while True:
    password = input("请输入需要检查的密码组合：")
    digits = len(password)  # 将输入的字符串长度赋给变量digits
    letter = number = symbol = 0  # 为字母、数字、符号分别设置一个标签并初始化为0

    for i in Letter:
        if i in password:
            letter = 1  # 当Letter中的元素在password中出现时，letter = 1
            break

    for j in Number:
        if j in password:
            number = 1  # 当Number中的元素在password中出现时，number = 1
            break

    for k in Symbol:
        if k in password:
            symbol = 1  # 当Symbol中的元素在password中出现时，symbol = 1
            break

    strength = letter + number + symbol  # strength为密码中的字符种类数

    # 根据密码长度和字符种类数将密码分为9个安全级别
    if digits <= 8 and (strength == 1):
        print_class("极低")

    elif 8 < digits < 16 and (strength == 1):
        print_class("很低")

    elif digits >= 16 and (strength == 1):
        print_class("低")

    elif digits <= 8 and (strength == 2):
        print_class("较低")

    elif digits <= 8 and (strength == 3):
        print_class("较高")

    elif 8 < digits < 16 and (strength == 2):
        print_class("高")

    elif digits >= 16 and (strength == 2):
        print_class("很高")

    elif 8 < digits < 16 and (strength == 3):
        print_class("极高")

    else:
        print("您的密码安全级别评定为：∞\n\
请继续保持！\n")
