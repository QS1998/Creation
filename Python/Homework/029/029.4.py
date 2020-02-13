#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/13 20:36
# User    : Magic
# Product : PyCharm
# Project : 029
# File    : 029.4.py
# Intro   : 全部替换


# def replace_all(file_name, old_keywords, new_keywords):
#     old_len = len(old_keywords)
#     with open(file_name, 'r+') as f:
#         content = f.read()
#         con_len = len(content)
#         indexes = []
#         counts = 0
#         for i in range(con_len):
#             if content[i:i + old_len] == old_keywords:
#                 indexes.append(i)
#                 counts += 1
#         answer = input("文件 %s 中共有%d个【%s】\n"
#                        "您确定把所有的【%s】替换为【%s】吗？\n"
#                        "【Y/N】:" % (file_name, counts, old_keywords, old_keywords, new_keywords))
#         if answer == 'Y':
#             for j in indexes:
#                 content = content[:j] + new_keywords + content[j + old_len:]
#             f.seek(0, 0)
#             f.truncate()
#             f.write(content)
#             print("替换成功!")
#
#
# name_of_file = input("请输入文件名:")
# old_word = input("请输入需要替换的单词或字符:")
# new_word = input("请输入新的单词或字符:")
#
# replace_all(name_of_file, old_word, new_word)



def file_replace(file_name, rep_word, new_word):
    f_read = open(file_name)

    content = []
    count = 0

    for eachline in f_read:
        if rep_word in eachline:
            count = eachline.count(rep_word) #count感觉应该用这个
            eachline = eachline.replace(rep_word, new_word)
        content.append(eachline)

    decide = input('\n文件 %s 中共有%s个【%s】\n您确定要把所有的【%s】替换为【%s】吗？\n【YES/NO】：' \
                   % (file_name, count, rep_word, rep_word, new_word))

    if decide in ['YES', 'Yes', 'yes']:
        f_write = open(file_name, 'w')
        f_write.writelines(content)
        f_write.close()

    f_read.close()


file_name = input('请输入文件名：')
rep_word = input('请输入需要替换的单词或字符：')
new_word = input('请输入新的单词或字符：')
file_replace(file_name, rep_word, new_word)
