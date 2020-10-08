#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   把元组用作记录
import os

lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

print('把元组用作记录：')
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# for循环可以分别提取元组里的元素，叫全拆包（unpacking）
# 因为元组中第二个元素对我们没有什么用，它赋值给"_"占位符
print('打印出国家：')
for country, _ in traveler_ids:
    print(country)

print('元组拆包：')
lax_coordinates = (33.9425, -118.408056)
latitude, longitude = lax_coordinates
print(latitude)
print(longitude)

print('可以使用*运算符把一个可迭代对象拆开作为函数的参数：')
print(divmod(20, 8))
t = (20, 8)
print(divmod(*t))
quotient, remainder = divmod(*t)
print(quotient, remainder)

print('元组拆包：让一个函数可以用元组的形式返回一多个值，然后调用函数的代码就能轻松地接受这些返回值：')
_, filename = os.path.split('/2_7_tuple_records.py')
print(filename)
