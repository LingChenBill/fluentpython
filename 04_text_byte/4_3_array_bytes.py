#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   使用数组中原始数据初始化bytes对象
import array

print('指定类型代码h，创建一个短整数（16位）数组：')
numbers = array.array('h', [-2, -1, 0, 1, 2])
print('octets保存组成numbers的字节序列的副本：')
octets = bytes(numbers)
print(octets)

