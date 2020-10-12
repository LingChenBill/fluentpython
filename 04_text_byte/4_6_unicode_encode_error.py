#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   编码成字节序列，成功和错误处理

city = 'São Paulo'
print('UTF_?能够处理任何字符串：')
print(city.encode('utf_8'))
print(city.encode('utf_16'))

print('iso8859_1处理：')
print(city.encode('iso8859_1'))

print('cp437无法编码: ')
# UnicodeEncodeError: 'charmap' codec can't encode character '\xe3' in position 1: character maps to <undefined>
# print(city.encode('cp437'))

print('errors=ignore处理方式跳过无法编码的字符，做法不妥：')
print(city.encode('cp437', errors='ignore'))

print('errors=replace把无法编码的字符替换成？: ')
print(city.encode('cp437', errors='replace'))

print('errors=xmlcharrefreplace把无法编码的字符替换成xml实体: ')
print(city.encode('cp437', errors='xmlcharrefreplace'))

