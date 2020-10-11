#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   UserDict它不但把所有的键都以字符串的形式存储
#   还能处理一些创建或者更新实例时包含非
import collections


class StrKeyDict(collections.UserDict):
    """
    StrKeyDict是对UserDict的扩展
    """
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[key]

    def __contains__(self, item):
        # 放心假设所有已经存储的键都是字符串
        return str(item) in self.data

    def __setitem__(self, key, value):
        # 会把所有的键都转换成字符串，
        self.data[str(key)] = value


print('测试StrKeyDict0，__missing__操作：')
d = StrKeyDict([('2', 'two'), ('4', 'four')])
# print(d['2'])
# print(d['4'])

# RecursionError: maximum recursion depth exceeded while calling a Python object
# print(d[4])
# print(d[1])
# print(d.get(1, 'N/A'))

# print(d.get('2'))

print(d.get('4'))

