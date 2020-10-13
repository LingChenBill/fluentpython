#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/13
# @Author: Lingchen
# @Prescription:
#   为了正确比较而规范化Unicode字符串
from unicodedata import normalize

s1 = 'café'
s2 = 'cafe\u0301'

print('s1与s2: ')
print(s1, s2)

print('s1与s2的长度：')
print(len(s1), len(s2))

print('比较s1与s2: ')
print(s1 == s2)

print('NFC使用最少的码位构成等价的字符串：')
print('NFC之后的s1与s2长度: ')
print(len(normalize('NFC', s1)), len(normalize('NFC', s2)))

print('NFD把组合字符分解成基字符和单独的组合字符：')
print('NFD之后的s1与s2长度: ')
print(len(normalize('NFD', s1)), len(normalize('NFD', s2)))

print(normalize('NFC', s1) == normalize('NFC', s2))

print(normalize('NFD', s1) == normalize('NFD', s2))

