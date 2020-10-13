#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/13
# @Author: Lingchen
# @Prescription:
#   一个平台上编码问题，（可能发生，也可以不会发生）

print('写入文件指定了UTF_8编码，但是读取文件时没有这么做：')
open('../data/cafe.txt', 'w', encoding='utf_8').write('café')

print('若打开文件是为了写入，但是没有指定编码参数，会使用区域设置中的默认编码，而且使用那个编码也能正确读取文件：')
print(open('../data/cafe.txt').read())


