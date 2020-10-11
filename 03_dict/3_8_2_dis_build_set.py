#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   用dis.dis(反汇编函数)来看看两个方法的字符码的不同
from dis import dis

print('检查{1}字面量背后的字节码：')
print('特殊的字节码BUILD_SET几乎完成了所有的工作：')
print(dis('{1}'))

print('set([1])的构造：')
print(dis('set([1])'))

print('frozenset的特殊字面量句法：')
print(frozenset(range(10)))


