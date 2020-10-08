#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   序列的增量赋值
#   不要把可变对象放在元组里面
#   增量赋值不是一个原子操作，虽然抛出了异常，但还是完成了操作

my_list = [1, 2, 3]
print(my_list)
print(id(my_list))

print('*=操作：')
my_list *= 2
print(my_list)
print(id(my_list))

print('Tuple t：')
t = (1, 2, 3)
print(t)
print(id(t))

print('Tuple *=：')
t *= 2
print(t)
print(id(t))

print('+=的谜题：')
t = (1, 2, [30, 40])
print(t)
print('+=操作：')
# 'tuple' object does not support item assignment
t[2] += [50, 60]
# t：(1, 2, [30, 40, 50, 60])
print(t)
