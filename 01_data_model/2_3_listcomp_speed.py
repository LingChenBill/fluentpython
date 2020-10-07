#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/7
# @Author: Lingchen
# @Prescription:
#   用列表推导和map/filter组合来创建同样的表单

symbols = '$¢£¥€¤'

print('列表推导： ')
beyond_ascii = [ord(s) for s in symbols if ord(s) > 127]
print(beyond_ascii)

print('map/filter: ')
beyond_ascii = list(filter(lambda c: c > 127, map(ord, symbols)))
print(beyond_ascii)
