#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   在元组拆包中使用*也可以帮助我们把注意力集中在元组的部分元素上

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2)
print(a, b, rest)

print('在平行赋值中，*前缀只能用在一个变量名前面，而这个变量可以出现在赋值表达式的任意位置：')
a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)
