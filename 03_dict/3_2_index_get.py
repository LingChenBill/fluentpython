#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/10
# @Author: Lingchen
# @Prescription:
#   从索引中获取单词出现的频率信息，并把它们写进对应的列表里
#   python3 3_2_index_get.py ../data/zen.txt
import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            # 提取word出现的情况，若还没有它的记录，返回[]
            occurrences = index.get(word, [])
            # 把单词新出现的位置添加到列表的后面
            occurrences.append(location)
            # 把新的列表放回字典中，这又牵扯到一次查询操作
            index[word] = occurrences

# 每一行的列表都代表了一个单词的出现情况
# 列表中的元素是一对值，第一个值表示出现的行，第二个表示出现的列
for word in sorted(index, key=str.upper):
    print(word, index[word])
