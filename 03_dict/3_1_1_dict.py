#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/9
# @Author: Lingchen
# @Prescription:
#   泛映射类型
from collections import abc

print('collections.abc中的MutableMapping: ')
my_dict = {}
print(isinstance(my_dict, abc.Mapping))

tt = (1, 2, (30, 40))
print(hash(tt))

print('只有当所有这些内部状态都是不可变的，这个对象才是可散列的：')
t1 = (1, 2, [30, 40])
# print('TypeError: unhashable type: 'list'')
# print(hash(t1))

tf = (1, 2, frozenset([30, 40]))
print(hash(tf))

print('字典提供了很多种构造方法：')
a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
d = dict([('two', 2), ('one', 1), ('three', 3)])
e = dict({'three': 3, 'one': 1, 'two': 2})
print(a == b == c == d == e)
