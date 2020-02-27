import copy

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
board0 = copy.deepcopy(board)
minn = 64
for x in range(N-7):
    for y in range(M-7):
        for k in range(2):
            cnt = 0
            board = copy.deepcopy(board0)
            if k == 0:
                board[x][y] = 'W'
            else:
                board[x][y] = 'B'
            for i in range(x, x+8):
                for j in range(y, y+8):
                    if (i, j) == (x, y):
                        continue
                    elif board[i][j] == board[i][j-1] and board[i][j] == 'B':
                        board[i][j] = 'W'
                        cnt += 1
                    elif board[i][j] == board[i][j-1] and board[i][j] == 'W':
                        board[i][j] = 'B'
                        cnt += 1
        if cnt < minn:
            minn = cnt
            print(x, y, minn)
print(minn)