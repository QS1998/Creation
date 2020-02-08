#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author  : Lysander Tseng
# Email   : 2474798826@qq.com
# Time    : 2020/2/6 15:45
# User    : Magic
# Product : PyCharm
# Project : 021
# File    : 021.0.py
# Intro   : No Description


# test = lambda x, y=3: x * y
#
#
# def d_s(x):
#     return x if x & 1 else None
#
#
# test_list = list(filter(lambda x : x % 3 == 0, range(101)))
#
# list_analytic = [x for x in range(101) if x % 3 == 0]
#
#
# def zip_custom(list1, list2):
#     list_length = min(len(list1), len(list2))
#     raw_list = []
#     for i in range(list_length):
#         element = [list1[i], list2[i]]
#         raw_list.append(element)
#     return raw_list
#
#
# processed_list1 = zip_custom([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
#
# processed_list2 = list(map(lambda x : list(x), [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]))
#
# processed_list3 = list(map(lambda x, y : [x, y], [1, 3, 5, 7, 9], [2, 4, 6, 8, 10]))
#
#
# def make_repeat(n):
#     return lambda s: s * n
#
#
# double = make_repeat(2)
# print(double(8))
# print(double('FishC'))
