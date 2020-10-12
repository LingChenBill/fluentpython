#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/12
# @Author: Lingchen
# @Prescription:
#   使用memoryview和struct查看一个GIF图像的首部
import struct

# 结构体的格式：<是小字节序，3s3s是两个3字节序列，HH是两个16位二进制整数
fmt = '<3s3sHH'

with open('../data/loading.gif', 'rb') as fp:
    img = memoryview(fp.read())

# 使用它的切片再创建一个memoryview对象，这里不会复制字节序列
header = img[:10]
print('转换成字节序列，这只是为了显示，这里复制了10字节：')
print(bytes(header))

print('拆包memoryview对象，得到一个元组，包含类型、版本、宽度和高度：')
unpack_header = struct.unpack(fmt, header)
print(unpack_header)

# 删除引用，释放memoryview实例所占用的内存
del header
del img

