#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/9
# @Author: Lingchen
# @Prescription:
#   字典推导（dictcomp）可以从任何以键值对作为元素的可迭代对象中构建出字典

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

print('把配好对的数据左右换了下，国家名是键，区域码是值：')
country_code = {country: code for code, country in DIAL_CODES}
print(country_code)

print('用区域码作为键，国家名转换为大写，并且过滤掉区域码大于或等于66的地区：')
new_country = {code: country.upper() for country, code in country_code.items()
               if code < 66}
print(new_country)
