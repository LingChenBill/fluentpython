#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   利用memoryview精准地修改了一个数组的某个字节
#   内存视图其实是泛化和去数字化的Numpy数组
#   通过改变数组中的一个字节来更新数组里某个元素的值
import array

my_number = array.array('h', [-2, -1, 0, 1, 2])
# 利用含有5个短整形有符号整数的数组（类型码：h）创建一个memoryview
memv = memoryview(my_number)
print(my_number)
print(len(memv))

print('第一个：')
print(memv[0])

# 创建一个memv_oct，把memv里的内容转换成'B'类型，也就是无符号字符
memv_oct = memv.cast('B')
# 以列表的形式查看memv_oct的内容
print(memv_oct.tolist())

memv_oct[5] = 4
print(my_number)
