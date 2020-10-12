#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   把字节序列解码成字符串，成功与失败

octets = b'Montr\xe9al'
print('使用cp1252解码，它是latin1的有效超集：')
print(octets.decode('cp1252'))

print('iso8859_7用于编码希腊文，不能解码\xe9: ')
print(octets.decode('iso8859_7'))

print('koi8_r解码：')
print(octets.decode('koi8_r'))

print('utf_8解码失败：')
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 5: invalid continuation byte
# print(octets.decode('utf_8'))

print(octets.decode('utf_8', errors='replace'))
