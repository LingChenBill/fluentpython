#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/13
# @Author: Lingchen
# @Prescription:
#   用户输入的文本默认是NFC形式
#   安全起见，保存文本之前，最好使用normalize('NFC', user_text)清洗文本
from unicodedata import normalize, name

ohm = '\u2126'
print(name(ohm))

ohm_c = normalize('NFC', ohm)
print(name(ohm_c))

print(ohm == ohm_c)

print(normalize('NFC', ohm) == normalize('NFC', ohm_c))
