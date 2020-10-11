#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   collections.Counter这个映射类型会给键准备一个整数计数器，
#   每次更新一个键的时候都会增加这个计数器
import collections

ct = collections.Counter('abracadabra')
print(ct)

print('collections.Counter的更新操作：')
ct.update('aaaaazzz')
print(ct)

print('ct.most_common会按照次序返回映射里最常见的n个键和它们的计数: ')
print(ct.most_common(2))


