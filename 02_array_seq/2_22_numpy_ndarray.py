#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/9
# @Author: Lingchen
# @Prescription:
#   对numpy.ndarray的行和列进行基本操作
import numpy

print('numpy.arange: ')
a = numpy.arange(12)
print(a)

print('Type: ')
print(type(a))

print('查看数组的维度: ')
print(a.shape)

print('把数组变成二维的，打印出来: ')
a.shape = 3, 4
print(a)
print(a[2])

print('打印元素: ')
print(a[2][1])

print('把第1列打印出来: ')
print(a[:, 1])

print('把行和列交换，得到新的数组: ')
print(a.transpose())
