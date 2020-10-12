#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   bytes和bytearray对象的各个元素是介于0~255（含）之间的整数

print('bytes对象可以从str对象使用给定的编码构建: ')
cafe = bytes('café', encoding='utf_8')
print(cafe)

print('各个元素都是range(255)内的整数: ')
print(cafe[0])

print('bytes对象的切片还是bytes对象，即使是只有一个字节的切片：')
print(cafe[:1])

print('bytearray对象没有字面量句法，而是以bytearray()和字节序列字面量参数的形式显示: ')
cafe_arr = bytearray(cafe)
print(cafe_arr)

print('bytearray对象的切片还是bytearray对象：')
print(cafe_arr[-1:])

print('二进制序列的fromhex是解析十六进制数字对，构建二进制序列：')
print(bytes.fromhex('31 4B CE A9'))

