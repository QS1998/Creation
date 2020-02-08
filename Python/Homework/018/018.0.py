#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/5 13:57
# User    : Magic
# Product : PyCharm
# Project : 018
# File    : 018.0.py
# Intro   : No Description


# 编写一个奇怪的函数😂
def strange_function(*para):  # 使用收集参数负责将接收到的数据打包传递给局部变量
    """0. 编写一个符合以下要求的函数：
          a) 计算打印所有参数的和乘以基数（base=3）的结果
          b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。
    """
    
    list_length = len(para)  # 计算列表长度并赋值给变量list_length
    list_sum = 0  # 初始化列表和的值为零

    # 用条件表达式当最后一个参数为'5'时base, sum_length = 5, list_length - 1;否则base, sum_length = 3, list_length
    base, sum_length = (5, list_length - 1) if para[-1] == '5' else (3, list_length)

    # 对收集参数进行求和
    for i in range(sum_length):
        list_sum += int(para[i])

    return list_sum * base  # 返回参数的和与base的积


string_in = input("请输入整形数据并以空格隔开:")
list_temp = string_in.split()  # 利用字符串方法将输入的字符串切片为列表保存在临时列表中
print(strange_function(*list_temp))  # 将临时列表中的参数解包再传递给奇异函数
