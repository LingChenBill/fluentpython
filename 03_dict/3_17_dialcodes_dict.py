#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/11
# @Author: Lingchen
# @Prescription:
#   将同样的数据以不同的顺序添加到3个字典中

DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

d1 = dict(DIAL_CODES)
print('d1: ', d1.keys())

print('sorted dict: ')
d2 = dict(sorted(DIAL_CODES))
print('d2: ', d2.keys())

print('数据的元组的顺序是按照国家名字的英文拼写来决定：')
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
print('d3: ', d3.keys())

print('上面这些字典是相等的，因为它们所包含的数据是一样的：')
print(d1 == d2 and d2 == d3)


