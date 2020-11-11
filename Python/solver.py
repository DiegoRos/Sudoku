from sudoku_functions import *
from time import time
def solveBoard(base, board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in base:
        if validNum(row,col,i,board):
            board[row][col] = i

            if solveBoard(base, board):
                return True

            board[row][col] = 0
    return False

def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None


def solver(board):
    base = list(range(1, len(board) + 1))
    solveBoard(base, board)
    return board


if __name__ == '__main__':
    start = time()
    board = [[0, 6, 2, 0, 1, 7, 0, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 2, 0],
             [0, 5, 0, 0, 0, 0, 7, 0, 0],
             [0, 0, 0, 2, 0, 0, 0, 6, 9],
             [0, 4, 1, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 8, 9, 0, 0, 0, 0],
             [1, 0, 0, 0, 7, 4, 0, 0, 5],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [3, 0, 0, 0, 5, 0, 1, 0, 0]]

    print(solver(board))
    print("Time Elapsed: ", time()-start)