#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   根据一个分数，找到它所对应的成绩
import bisect


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    """
    查找分数对应的等级
    :param score:
    :param breakpoints:
    :param grades:
    :return:
    """
    i = bisect.bisect(breakpoints, score)
    return grades[i]


my_grade = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
print(my_grade)
