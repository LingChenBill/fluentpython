#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   用生成器表达式初始化元组和数组
import array

symbols = '$¢£¥€¤'
tuple_new = tuple(ord(symbol) for symbol in symbols)
print('用生成器表达式初始化元组和数组：')
print(tuple_new)

array_new = array.array('I', (ord(symbol) for symbol in symbols))
print('用array构造方法来构造数组：')
print(array_new)
