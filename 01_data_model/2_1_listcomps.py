#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/7
# @Author: Lingchen
# @Prescription:
#   列表推导（list comprehension）简称listcomps
#       原则：只用列表推导来创建新的列表，并且尽量保持简短。
#            若列表推导的代码超过了2行，就要考虑是不是得用for循环重写了
#   生成式表达器（generator expression）则称为genexps

symbols = '$¢£¥€¤'
codes = []
for symbol in symbols:
    # 返回字母的unicode的整数值
    codes.append(ord(symbol))

print(codes)

print('listcomps: ')
codes_list = [ord(symbol) for symbol in symbols]
print(codes_list)