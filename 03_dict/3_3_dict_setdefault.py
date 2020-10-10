#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/10
# @Author: Lingchen
# @Prescription:
#   从索引中获取单词出现的频率信息，并把它们写进对应的列表里
#   用 setdefault() 一行解决了获取和更新单词的出现情况列表
#   python3 3_3_dict_setdefault.py ../data/zen.txt
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
            # # 提取word出现的情况，若还没有它的记录，返回[]
            # occurrences = index.get(word, [])
            # # 把单词新出现的位置添加到列表的后面
            # occurrences.append(location)
            # # 把新的列表放回字典中，这又牵扯到一次查询操作
            # index[word] = occurrences

            # 获取单词的出现情况列表，若单词不存在，把单词和一个空列表放进映射，然后返回这个空列表，
            # 这样就能在不进行第二次查找的情况下更新列表了
            index.setdefault(word, []).append(location)

# 每一行的列表都代表了一个单词的出现情况
# 列表中的元素是一对值，第一个值表示出现的行，第二个表示出现的列
for word in sorted(index, key=str.upper):
    print(word, index[word])
