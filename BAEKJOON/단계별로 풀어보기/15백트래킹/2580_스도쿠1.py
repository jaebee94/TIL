for i in range(0, 9, 3):
    for j in range(0, 9, 3):
        for x in range(i, i+3):
            for y in range(j, j+3):
                if board[x][y] != 0:
                    cnt += 1
        if cnt


board = [list(map(int, input().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if board[i][j] == 0:
            zeros.append((i, j))
sudoku(0)