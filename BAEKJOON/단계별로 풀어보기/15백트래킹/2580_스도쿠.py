import sys

def horizon(x, num):
    for i in range(9):
        if num == board[x][i]:
            return False
    return True


def vertical(y, num):
    for i in range(9):
        if num == board[i][y]:
            return False
    return True


def square(x, y, num):
    for i in range(x//3 * 3, x//3 * 3 + 3):
        for j in range(y//3 * 3, y//3 * 3 + 3):
            if num == board[i][j]:
                return False
    return True


def sudoku(a):
    if a == len(zeros):
        for line in board:
            print(' '.join(map(str, line)))
        sys.exit(0)
    else:
        zerox = zeros[a][0]
        zeroy = zeros[a][1]
        for i in range(1, 10):
            if horizon(zerox, i) and vertical(zeroy, i) and square(zerox, zeroy, i):
                board[zerox][zeroy] = i
                sudoku(a+1)
                board[zerox][zeroy] = 0


board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))
sudoku(0)