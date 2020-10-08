#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   insort可以保持有序序列的顺序
#   如果你只需要处理数字列表的话，数组可能是个更好的选择
import bisect
import random

SIZE = 7

random.seed(1729)
my_list = []
for i in range(SIZE):
    new_item = random.randrange(SIZE * 2)
    bisect.insort(my_list, new_item)
    print('%2d -> ' % new_item, my_list)

