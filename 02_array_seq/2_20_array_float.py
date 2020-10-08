#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   一个浮点型数组的创建、存入文件和从文件读取的过程
#   若需要一个只包含数字的列表，那么array.array比list更高效
from array import array
from random import random

print('利用一个可迭代对象来建立一个双精度浮点数组（类型码是d）：')
my_floats = array('d', (random() for i in range(10**7)))
print(my_floats[-1])

# 把数组存入一个二进制文件里
fp = open('2_20_floats.bin', 'wb')
my_floats.tofile(fp)
fp.close()

my_floats2 = array('d')
fp = open('2_20_floats.bin', 'rb')
my_floats2.fromfile(fp, 10**7)
fp.close()
print(my_floats2[-1])

print('存入前与读取后的array是否相等：')
print(my_floats == my_floats2)
