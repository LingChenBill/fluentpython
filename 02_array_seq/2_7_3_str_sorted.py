#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   list.sort方法和内置函数sorted
#   list.sort返回None
#   sorted可以返回一个新的对象

print('sorted：')
fruits = ['grape', 'raspberry', 'apple', 'banana']
print(fruits)
print(sorted(fruits))

print('排序且反序：')
print(sorted(fruits, reverse=True))

print('用元素长度且排序：')
print(sorted(fruits, key=len))

print('sort()操作：')
print(fruits)
fruits.sort()
# None
# print(fruits.sort())
print(fruits)
