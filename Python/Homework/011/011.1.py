#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/2 9:32
# User    : Magic
# Product : PyCharm
# Project : 011
# File    : 011.1.py
# Intro   : No Description


list1 = [
      '1.Just Do It',
      '2.一切皆有可能',
      '3.让编程改变世界',
      '4.Impossible is Nothing']

list2 = [
      '4.阿迪达斯',
      '2.李宁',
      '3.鱼C工作室',
      '1.耐克']

list3 = [name + ':' + slogan[2:] for name in list2 for slogan in list1 if name[0] == slogan[0]]
list3.sort()

print(list1)
print(list2)
print(list3)