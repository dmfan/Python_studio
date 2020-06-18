#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 数据结构和算法2



"""
递归回溯法：叫称为试探法，按选优条件向前搜索，当搜索到某一步，发现原先选择并不优或达不到目标时，就退回一步重新选择，比较经典的问题包括骑士巡逻、八皇后和迷宫寻路等。
骑士巡逻
是指在按照国际象棋中骑士的规定走法走遍整个棋盘的每一个方格，而且每个网格只能夠经过一次。由骑士巡逻引申出了一个著名的数学问题 ：骑士巡逻问题--找出所有的骑士巡逻路径。
"""
import sys
import time

SIZE = 5
total = 0


def print_board(board):
    for row in board:
        for col in row:
            print(str(col).center(4), end='')
        print()


def patrol(board, row, col, step=1):                    # 递归调用
    if row >= 0 and row < SIZE and \
        col >= 0 and col < SIZE and \
        board[row][col] == 0:
        board[row][col] = step
        if step == SIZE * SIZE:                         # 每一步走一个格，不走重复格，经过 SIZE * SIZE 步就走完所有格。     本程序起点位于棋盘右下角
            global total
            total += 1
            print(f'第{total}种走法: ')
            print_board(board)
        # 国际象棋中的骑士有八种走法               # 每一步去遍历八种走法，摈弃超出棋盘的方法
        patrol(board, row - 2, col - 1, step + 1)   #四 左走两格向后走一格
        patrol(board, row - 1, col - 2, step + 1)   #二 左走一格向后走两格
        patrol(board, row + 1, col - 2, step + 1)   #六 右走一格向后走两格
        patrol(board, row + 2, col - 1, step + 1)   #八 右走两格向后走一格
        patrol(board, row + 2, col + 1, step + 1)   #七 右走两格向前走一格
        patrol(board, row + 1, col + 2, step + 1)   #五 右走一格向前走两格
        patrol(board, row - 1, col + 2, step + 1)   #一 左走一格向前走两格
        patrol(board, row - 2, col + 1, step + 1)   #三 左走两格向前走一格
        board[row][col] = 0


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    patrol(board, SIZE - 1, SIZE - 1)


if __name__ == '__main__':
    main()