#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/13
# @Author: Lingchen
# @Prescription:
#   仔细分析读取文件
import os

print('默认情况下，open函数采用文本模式：')
fp = open('../data/cafe.txt', 'w', encoding='utf_8')
print(fp)

fp.write('café')
fp.close()

print('os.stat报告文件中有多少个字节：')
print(os.stat('../data/cafe.txt').st_size)

print('打开文件没有指明字节码，编码是区域设置里的默认值：')
fp2 = open('../data/cafe.txt')
print(fp2)

print('fp2的默认编码：')
print(fp2.encoding)

print('读取文件：')
print(fp2.read())

print('打开文件指定文件编码：')
fp3 = open('../data/cafe.txt', encoding='utf_8')
print(fp3)

print('文件编码：')
print(fp3.encoding)

print('读取文件：')
print(fp3.read())

print('打开文件指定标志 rb 在二进制模式中读取文件：')
fp4 = open('../data/cafe.txt', 'rb')
print(fp4)

print('读取文件：')
print(fp4.read())

