import numpy as np

def validBoard(board):
    base = list(range(1, len(board) + 1))
    divisions = factors(len(board))

    for i in range(len(board)):
        if not len(board) == len(board[i]):
            return False
    row_check = board
    column_check = np.transpose(board)
    for row, column in zip(row_check,column_check):
        row, column = list(row), list(column)
        for i in base:
            if row.count(i) > 1 or column.count(i) > 1:
                return False
    start_row = 0
    for _ in range(divisions[1]):
        start_column = 0
        for _ in range(divisions[0]):
            box_check = []
            for i in range(start_row, start_row + divisions[0]):
                for j in range(start_column, start_column + divisions[1]):
                    box_check.append(board[i][j])

            for i in base:
                if box_check.count(i) > 1:
                    return False
            start_column += divisions[1]
        start_row += divisions[0]
    return True

def validNum(x,y,val,board):
    base = list(range(1, len(board) + 1))
    divisions = factors(len(board))
    boxes = startBox(divisions, board)
    test_board = board
    for i in range(len(base)):
        if test_board[x][i] == val:
            return False

    for i in range(len(base)):
        if test_board[i][y] == val:
            return False

    current_box = []
    for box_row in boxes[0]:
        for box_col in boxes[1]:
            if box_row <= x < box_row + divisions[0] and box_col <= y < box_col + divisions[1]:
                current_box.append(box_row)
                current_box.append(box_col)
    box_check = []
    for i in range(current_box[0], current_box[0] + divisions[0]):
        for j in range(current_box[1], current_box[1] + divisions[1]):
            box_check.append(test_board[i][j])
    for i in box_check:
        if i == val:
            return False

    return True

def factors(num):
    test_num = int(np.sqrt(num))
    while num%test_num != 0:
        test_num -= 1
    return test_num, int(num/test_num)


def startBox(divisions,board):
    start_box_row = []
    start_box_col = []
    for i in range(0,len(board),divisions[0]):
        start_box_row.append(i)
    for i in range(0,len(board),divisions[1]):
        start_box_col.append(i)
    return [start_box_row, start_box_col]


def printBoard(board):
    divisions = factors(len(board))
    for i in range(len(board)):
        if i % divisions[0] == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(board[i])):
            if j % divisions[1] == 0 and j != 0:
                print(' | ', end = '')
            print(board[i][j], end = ' ')
        print()