def confirmation(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return False
    return True

def queen(i, j):
    board[i][j] = 1
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        while 0 <= ni < N and 0 <= nj < N:
            board[ni][nj] = 1
            ni += di[k]
            nj += dj[k]

def returnqueen(i, j):
    board[i][j] = 0
    for k in range(8):
        ni = i + di[k]
        nj = j + dj[k]
        while 0 <= ni < N and 0 <= nj < N:
            board[ni][nj] = 0
            ni += di[k]
            nj += dj[k]


N = int(input())
board = [[0]*N for _ in range(N)]
di = [0, 1, 1, 1, 0, -1, -1, -1]
dj = [1, 1, 0, -1, -1, -1, 0, 1]
result = 0

# for i in range(N):
#     print(board[i])

for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            queen(i, j)
            tmpx, tmpy = i, j
if confirmation(board):
    cnt += 1