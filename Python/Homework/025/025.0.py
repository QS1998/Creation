#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/10 18:14
# User    : Magic
# Product : PyCharm
# Project : 025
# File    : 025.0.py
# Intro   : 编写一个简易通讯录
print("|---欢迎进入通讯录程序---|")


# 定义一个decision1函数用于判断用户指令
def decision1(name):
    while True:
        judge = input("该联系人不存在!\n"  # 当要查找的联系人不存在时，询问用户是否需要新建联系人
                      "是否添加联系人?(Y/N):")

        # 判断用户输入Y/N/other，分别执行相应操作，完事后用break退出循环或是用continue进入下次循环
        if judge == 'Y':
            print("请输入联系人'{0}'的联系电话:".format(name))
            number = input()
            address_book[name] = number
            print("数据已保存！")
            break
        elif judge == 'N':
            break
        else:
            print("格式错误!请重新输入!")
        continue


# 定义一个decision2函数用于判断用户指令
def decision2(name):
    while True:
        judge = input("是否修改用户资料?(Y/N):")  # 当要新建的联系人已存在时，询问用户是否需要更新联系人信息

        # 判断用户输入Y/N/other，分别执行相应操作，完事后用break退出循环或是用continue进入下次循环
        if judge == 'Y':
            print("请输入联系人'{0}'的联系电话:".format(name))
            number = input()
            address_book[name] = number
            print("数据已保存！")
            break
        elif judge == 'N':
            break
        else:
            print("格式错误!请重新输入!")
        continue


address_book = {}  # 创建一个空字典，用于存放联系人及信息

while True:  # 程序在线运行

    print("""
|---1:查询联系人资料 ---|
|---2:插入新的联系人 ---|
|---3:删除已有联系人 ---|
|---4:退出通讯录程序 ---|""")
    order = input("请输入相关的指令代码:")

    # 判断用户指令，根据不同指令分别进行不同操作
    if order == '1':
        name1 = input("请输入联系人姓名:")

        # 判断用户输入的联系人是否在通讯录中，若是，则打印该联系人信息；否则调用decision1函数执行相关操作
        if name1 in address_book:
            print("{0} : {1}".format(name1, address_book[name1]))
        else:
            decision1(name1)
        continue  # 判断并执行完相关操作后执行continue语句回到开头

    elif order == '2':
        name2 = input("请输入新联系人姓名:")

        # 判断通讯录中是否已存在将要新建的联系人姓名，若通讯录中已存在该联系人，则告知用户该联系人已存在并打印该联系人信息；
        # 否则让用户进一步输入该联系人电话并保存在字典address_book中
        if name2 in address_book:
            print("您输入的姓名在通讯录中已存在!\n"
                  "{0} : {1}".format(name2, address_book[name2]))
            decision2(name2)

        else:
            number1 = input("请输入用户联系电话:")
            address_book[name2] = number1
            print("数据已保存!\n"
                  "{0} : {1}".format(name2, address_book[name2]))
        continue  # 判断并执行完相关操作后执行continue语句回到开头

    elif order == '3':
        name3 = input("请输入将要删除的联系人名称:")
        # 判断通讯录中是否已存在将要删除的联系人名称
        # 若存在，则进一步向用户确认是否删除
        #    若是，则删除该联系人
        #    若否，则退出循环
        #    若输入不是Y/N，则告知用户重新输入，并执行continue语句回到【确认是否删除】对话框
        # 若不存在，则告知用户【该联系人不存在】
        # 判断结束后执行continue语句回到开头指令输入对话框
        if name3 in address_book:
            while True:
                print("确定删除联系人{0}的相关信息吗?(Y/N)")
                judge3 = input()
                if judge3 == 'Y':
                    del address_book[name3]
                    print("成功删除!")
                    break
                elif judge3 == 'N':
                    break
                else:
                    print("格式错误!请重新输入!")
                    continue
        else:
            print("该联系人不存在!")
        continue

    elif order == '4':
        # 若用户输入的指令为4，则退出通讯录程序
        print("\n|---感谢使用通讯录程序---|")
        break

    # 若输入的数据非以上4种，则告知用户重新输入并执行continue语句回到开头指令输入界面
    else:
        print("格式错误!请重新输入!")
        continue
