#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   给切片赋值
#   把切片放在赋值语句的左边，或把它作为del操作的对象，
#   可以对序列进行嫁接、切除或就地修改操作

my_list = list(range(10))
print(my_list)

print('对切片进行赋值：')
# my_list[2:5] = [20, 30, 40]
my_list[2:5] = [20, 30]
print(my_list)

print('切片删除：')
del my_list[5:7]
print(my_list)

print('切片间隔赋值：')
my_list[3::2] = [11, 22]
print(my_list)

# my_list[2:5] = 100
# print(my_list)
print('赋值的对象是一个切片，那么赋值语句的右侧必须是个可迭代对象，即使只有单独一个值：')
print(my_list[2:5])
my_list[2:5] = [100]
print(my_list)

print('想把一个序列复制几份然后拼接起来，最快捷的做法是把这个序列乘以一个整数：')
my_num = [1, 2, 3]
print(my_num * 5)
print('+ 与 * 不修改原有的操作对象，而是构建一个全新的序列：')
print(5 * 'abcd')



