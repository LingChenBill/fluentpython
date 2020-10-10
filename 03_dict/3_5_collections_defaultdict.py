#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/10
# @Author: Lingchen
# @Prescription:
#   defaultdict: 处理找不到的键的一个选择
#   创建一个从单词到其出现情况的映射
#   python3 3_5_collections_defaultdict.py ../data/zen.txt
import sys
import re
import collections

WORD_RE = re.compile(r'\w+')

# 把list构造方法作为default_factory来创建一个defaultdict.
index = collections.defaultdict(list)
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 若index并没有word的记录，那么default_factory会被调用，为查询不到的键创造一个值。
            # 这个值在这里是一个空的列表，然后这个空列表被赋值给index[word],继而被当作返回值返回，
            # 因此append方法操作总会成功
            index[word].append(location)

# 以字母顺序打印出结果
for word in sorted(index, key=str.upper):
    print(word, index[word])

