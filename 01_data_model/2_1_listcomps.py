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

# for关键字之后的赋值操作可能会影响列表推导上下文中的同名变量，python3不会出现这种情况
# 在Python3中都有了自己的局部作用域，表达式内部的变量和赋值只在局部起作用
x = 'my precious'
dummy = [x for x in 'ABC']
print(x)

x = 'ABC'
dummy = [ord(x) for x in x]
print(x)
print(dummy)

