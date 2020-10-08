#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   使用列表推导计算笛卡尔积
#   列表推导的作用只有一个：生成列表
#   若想生成其他类型的序列，生成器表达式就派上了用场

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]
print('先以颜色排列，再以尺码排列：')
print(tshirts)

print('嵌套循环遍历：')
for color in colors:
    for size in sizes:
        print((color, size))

print('先按尺码，再按颜色来排列：')
tshirts = [(color, size) for size in sizes for color in colors]
print(tshirts)

