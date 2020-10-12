#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   把码位转换成字节序列的过程是编码，把字节序列转换成码位的过程是解码

s = 'café'
print('字符串的Unicode字符：')
print(len(s))

b = s.encode('utf8')
print('使用UTF8把str对象编码成bytes对象：')
print(b)

print('字节码中有多少字符：')
print(len(b))

d = b.decode('utf8')
print('使用UTF8把bytes解码成str对象：')
print(d)
