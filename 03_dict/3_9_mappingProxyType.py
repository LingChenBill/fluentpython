#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   用MappingProxyType来获取字典的只读实例mappingproxy
from types import MappingProxyType

d = {1: 'A'}
print('MappingProxyType: ')
d_proxy = MappingProxyType(d)
print(d_proxy)
# d中的内容可以通过d_proxy看到
print(d_proxy[1])

print('d_proxy赋值：')
# 通过d_proxy并不能做任何修改
# TypeError: 'mappingproxy' object does not support item assignment
# d_proxy[2] = 'x'

d[2] = 'x'
# d_proxy是动态的，也就是说对d所做的任何改动都会反馈到它上面
print(d_proxy)
