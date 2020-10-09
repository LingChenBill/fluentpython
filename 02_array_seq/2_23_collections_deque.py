#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/9
# @Author: Lingchen
# @Prescription:
#   使用双向队列
from collections import deque

print('队列可以容纳的元素的数量，而且一旦设定，这个属性就不能修改了：')
dq = deque(range(10), maxlen=10)
print(dq)

print('队列的旋转操作，n > 0: 队列的最右边的n个元素会被移动到最左边：')
dq.rotate(3)
print(dq)

print('队列的旋转操作，n < 0: 队列的最左边的n个元素会被移动到最右边：')
dq.rotate(-4)
print(dq)

print('当试图对一个已满的队列添加操作时，头部元素会被删除：')
dq.appendleft(-1)
print(dq)

print('一次添加多个元素：')
dq.extend([11, 22, 33])
print(dq)

print('左边添加元素：')
dq.extendleft([10, 20, 30, 40])
print(dq)
