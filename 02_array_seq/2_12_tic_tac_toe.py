#! /usr/bin/python3
# -*- coding:utf-8 -*-
# @Time: 2020/10/8
# @Author: Lingchen
# @Prescription:
#   过三关，是一种在3*3的方块矩阵上进行的游戏

print('井字游戏：')
board = [['_'] * 3 for i in range(3)]
print(board)

print('井字赋值：')
board[1][2] = 'X'
print(board)

print('含有3个指向同一对象的引用的列表是毫无用处的：')
weird_board = [['_'] * 3] * 3
print(weird_board)
weird_board[1][2] = 'O'
print(weird_board)

print('For循环，对象的引用：')
row = ['_'] * 3
weird_board = []
for i in range(3):
    weird_board.append(row)
print(weird_board)
weird_board[1][2] = 'P'
print(weird_board)

print('For循环，在循环里面初始化：')
board = []
for i in range(3):
    row = ['_'] * 3
    board.append(row)
print(board)
board[1][2] = 'X'
print(board)

