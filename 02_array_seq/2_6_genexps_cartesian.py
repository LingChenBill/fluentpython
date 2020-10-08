#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   使用生成器表达式计算笛卡尔积
#   生成器表达式逐个产出元素，从来不会一次性产出一个含有6个T恤样式的列表

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
print('使用生成器表达式计算笛卡尔积：')
for tshirt in ('(%s, %s)' % (c, s) for c in colors for s in sizes):
    print(tshirt)
