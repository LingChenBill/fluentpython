#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   编解码器编码字符串，得到的字节序列的差异

print('使用3个编解码器编码字符串，得到的字节序列的差异')
for codec in ['latin_1', 'utf_8', 'utf_16']:
    print(codec, 'Herr Voß'.encode(codec), sep='\t')
