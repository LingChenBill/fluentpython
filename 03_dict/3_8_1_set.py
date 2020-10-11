#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   set集合的本质是许多唯一对象的聚集
#   集合中的元素必须是可散列的，set类型本身是不可散列的，但是frozenset可以

print('set: ')
my_list= ['spam', 'spam', 'eggs', 'eggs']
print(set(my_list))

print('set -> list: ')
print(list(set(my_list)))

# needles的元素在haystack里出现的次数
# 要求两个对象都是集合
# found = len(needles & haystack)

# needles的元素在haystack里出现的次数，这次的代码可以用在任何可迭代的对象上
# found = len(set(needles) & set(haystack))

# found len(set(needles).intersection(haystack))

print('除了空集，集合的字符串表示形式总是以{...}的形式出现：')
s = {2}
print(type(s))

print(s)

print('POP：')
print(s.pop())

print('空集合：set()')
print(s)

