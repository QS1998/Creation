#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/3 9:21
# User    : Magic
# Product : PyCharm
# Project : 015
# File    : 015.0.py
# Intro   : 整数进制转换


# 定义一个二-十进制转换函数，未输入第二个参数则默认执行十转二；
# 有且值为-1时则执行二转十
def bin_fx(x, y=0):
    if y == -1:  # 二进制转十进制
        length = len(x)  # 定义剩余字符数变量
        result = 0  # 数值初始化
        for i in x:  # 遍历输入字符串中的字符
            if length > 0:
                j = int(i)
                result += j * 2 ** (length - 1)  # 由原理计算再累加得到数值结果
                length -= 1
        return '   ' + str(result)  # 将得到的整形数据结果再次转换为字符串返回
    else:  # 十进制转二进制
        i = int(x)
        result = ''  # 初始化字符串
        result_head = '0b '
        # 利用短除法原理求得转换后的数值并转换为字符串
        while i > 0:
            j = i % 2
            i = i // 2
            result += str(j)
        return result_head + result[::-1]
        # 利用列表的切片操作将进制头符号与结果连接起来


# 与bin_fx()函数实现逻辑相似
def oct_fx(x, y=0):
    if y == -1:
        length = len(x)
        result = 0
        for i in x:
            if length > 0:
                j = int(i)
                result += j * 8 ** (length - 1)
                length -= 1
        return '   ' + str(result)
    else:
        i = int(x)
        result = ''
        result_head = '0o '
        while i > 0:
            j = i % 8
            i = i // 8
            result += str(j)
        return result_head + result[::-1]


# 与bin_fx()函数实现逻辑相似
def hex_fx(x, y=0):
    if y == -1:
        length = len(x)
        result = 0
        for i in x:
            if length > 0:
                if i in letter:
                    j = ord(i) - 87  # 比对ASCII表将得到的a~f转换为数字10~15
                    result += j * 16 ** (length - 1)
                    length -= 1
                else:
                    j = int(i)  # 若数值为0~9，则直接转换为字符
                    result += j * 16 ** (length - 1)
                    length -= 1
        return '   ' + str(result)
    else:
        i = int(x)
        result = ''
        result_head = '0x '
        while i > 0:
            j = i % 16
            i = i // 16
            if chr(j + 87) in letter:
                result += chr(j + 87)  # 比对ASCII表对得到的10~15编码为字母a~f
            else:
                result += str(j)  # 若数值为0~9，则直接转换为字符
        return result_head + result[::-1]


# 定义一个进制选择函数，负责根据输入的进制类型判断应该调用哪一个以及
# 如何调用进制转换函数并将得到后的结果以规定格式打印在屏幕上
def choose():
    while 1:

        # 输入及异常处理
        temp = input("请输入进制:")
        if temp == "exit()":  # 加入一个退出判断语句
            print("正在退出程序...")
            break
        elif temp.isdigit():
            x = int(temp)
        else:
            print("进制格式错误！请重新输入！")
            continue
        num = input("请输入要转换的整数:")
        if num == "exit()":  # 加入一个退出判断语句
            print("正在退出程序...")
            break

        # 根据进制调用转换函数
        if x == 2:
            print("BIN:0b " + num)
            print("OCT:" + oct_fx(bin_fx(num, -1)))
            print("DEC:" + bin_fx(num, -1))
            print("HEX:" + hex_fx(bin_fx(num, -1)))
        elif x == 8:
            print("BIN:" + bin_fx(oct_fx(num, -1)))
            print("OCT:0o " + num)
            print("DEC:" + oct_fx(num, -1))
            print("HEX:" + hex_fx(oct_fx(num, -1)))
        elif x == 10:
            print("BIN:" + bin_fx(num))
            print("OCT:" + oct_fx(num))
            print("DEC:   " + num)
            print("HEX:" + hex_fx(num))
        elif x == 16:
            print("BIN:" + bin_fx(hex_fx(num, -1)))
            print("OCT:" + oct_fx(hex_fx(num, -1)))
            print("DEC:" + hex_fx(num, -1))
            print("HEX:0x " + num)
        else:
            print("抱歉，本程序暂不支持该进制！")


letter = "abcdef"  # 16进制的10~15
choose()
