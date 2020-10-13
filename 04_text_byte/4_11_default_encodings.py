#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/13
# @Author: Lingchen
# @Prescription:
#   探索编码默认值
#   遵从Unicode三明治的建议，而且始终在程序中显式的指定编码，那将避免很多问题
import sys, locale

print('文本文件默认使用locale.getpreferredencoding(): ')

expressions = """
    locale.getpreferredencoding()
    type(my_file)
    my_file.encoding
    sys.stdout.isatty()
    sys.stdout.encoding
    sys.stdin.isatty()
    sys.stdin.encoding
    sys.stderr.isatty()
    sys.stderr.encoding
    sys.getdefaultencoding()
    sys.getfilesystemencoding()
"""

my_file = open('../data/dummy', 'w')

for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))

