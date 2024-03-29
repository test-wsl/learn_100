#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


def print_board(board):
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])


def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'X'
        counter = 0
        # os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input('轮到{}走棋， 其输入位置：'.format(turn))
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                if turn == 'X':
                    turn = 'O'
                else:
                    turn = 'X'
            # os.system('cls')
            print_board(curr_board)
        choice = input("在玩一局？（yes|no）")
        begin = choice == 'yes'


if __name__ == '__main__':
    main()
