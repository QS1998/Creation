#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/1 8:49
# User    : Magic
# Product : PyCharm
# Project : 007
# File    : 007.0.py
# Intro   : No Description


def censor(temp):  # 定义一个字符检查函数：如果输入的不是整数，则重新输入;如果是整数，则以整型返回该整数
    while not temp.isdigit():
        print("输入错误，请重新输入：")
        temp = input()
    else:
        num = int(temp)
        return num


temp0 = input("请输入人数：")
censor(temp0)
people = int(temp0)  # 将经过初步审核的整型数据赋值给people这个变量

scores = []  # 创建一个空列表用于存储学生成绩
num_A = num_B = num_C = num_D = 0  # 初始化各成绩人数

for each in range(0, people):
    print("请输入第%d位学生的成绩：" % (each+1))
    temp1 = input()
    number = censor(temp1)
    scores.append(number)
    while not (0 <= scores[each] <= 100):  # 二次审核输入的整型数据是否落在[0,100]这个区间
        scores.pop()
        print("请重新输入第%d位学生的成绩：" % (each + 1))  # 若否，则重新输入
        temp1 = input()
        number = censor(temp1)
        scores.append(number)
    else:  # 若是，则执行else语句里的内容：对输入的的分数按照A、B、C、D四个等级进行分类
        if 60 <= scores[each] < 80:  # 按照成绩近似服从正态分布的原理优先对占比大的成绩进行判断
            print("C")
            num_C += 1
        elif scores[each] < 60:
            print("D")
            num_D += 1
        elif 80 <= scores[each] < 90:
            print("B")
            num_B += 1
        else:
            print("A")
            num_A += 1

print("成绩录入完毕！")
print("成绩为A的共有%d人\n"  # 将统计后的各成绩人数打印出来
      "成绩为B的共有%d人\n"
      "成绩为C的共有%d人\n"
      "成绩为D的共有%d人\n" % (num_A, num_B, num_C, num_D))
