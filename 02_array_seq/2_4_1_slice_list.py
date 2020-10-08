#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   切片和区间会忽略最后一个元素
#   s[a:b:c]这种用法只能作为索引或者下标用在[]中来返回一个切片对象

my_list = [10, 20, 30, 40, 50, 60]
print('在下标为2的地方进行向前分割：')
print(my_list[:2])

print('在下标为2的地方进行向后分割：')
print(my_list[2:])

print('在下标为3的地方进行向后分割：')
print(my_list[3:])

print('对对象进行切片：')
print('用s[a:b:c]的形式对s在a和b之间以c为间隔取值：')
s = 'bicycle'
print(s[::3])

print('s[a:b:c]c的值还可以为负，负值意味着反向取值：')
print(s[::-1])
print(s[::-2])


