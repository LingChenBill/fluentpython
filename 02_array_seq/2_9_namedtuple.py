#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   如何用具名元组来记录一个城市的信息
from collections import namedtuple

# 创建一个具名元组需要两个参数，一个是类名，另一个是类的各个字段的名字，由空格隔开
City = namedtuple('City', 'name country population coordinates')
tokyo = City('Tokyo', 'JP', 36.933, (35.689722, 139.691667))
print(tokyo)

print('具名元组可以通过字段名或者位置来获取一个字段的信息：')
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])

print('具名元组的属性和方法：')
# _fields属性是一个包含这个类所有字段名称的元组
print(City._fields)
LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi NCR', 'IN', 21.935, LatLong(28.613889, 77.208889))
# 用_make()通过接受一个可迭代对象来生成这个类的一个实例，它的作用跟City(*delhi_data)是一样的
# delhi = City(*delhi_data)
delhi = City._make(delhi_data)
# _asdict()把具名元组以collections.OrderedDict的形式返回，可以元组里的信息友好的呈现出来
print(delhi._asdict())

for key, value in delhi._asdict().items():
    print(key + ':', value)
