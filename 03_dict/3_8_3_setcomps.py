#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   集合推导
#   新建一个Latin-1字符集合，该集合里的每个字符的Unicode名字里都有"SIGN"这个单词
from unicodedata import name

print('把编码在32~255之间的字符的名字里有SIGN单词的挑出来，放到一个集合中：')
my_set = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i), '')}
print(my_set)
