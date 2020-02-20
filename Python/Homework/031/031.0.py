#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : qingshan.tseng@gmail.com
# Time    : 2020/2/19 10:42
# User    : Magic
# Product : PyCharm
# Project : 031
# File    : 031.0.py
# Intro   : No Description
import pickle


def dialogue_organize(file_name):
    """将文件文本中不同人的对话进行分离整理"""

    count = 1
    boy = []
    girl = []
    with open(file_name) as f:
        for each_line in f:
            if each_line.startswith('小甲鱼:'):
                boy.append(each_line[4:])
            elif each_line.startswith('小客服:'):
                girl.append(each_line[4:])
            else:
                with open(f'boy_{count}.pkl', mode='wb') as f1, open(f"girl_{count}.pkl", mode='wb') as f2:
                    pickle.dump(boy, f1)
                    boy.clear()
                    pickle.dump(girl, f2)
                    girl.clear()
                    count += 1
        else:
            with open(f'boy_{count}.pkl', mode='wb') as f1, open(f"girl_{count}.pkl", mode='wb') as f2:
                pickle.dump(boy, f1)
                boy.clear()
                pickle.dump(girl, f2)
                girl.clear()


actual_file_name = r'D:\Creation\Python\Homework\031\record.txt'
dialogue_organize(actual_file_name)
