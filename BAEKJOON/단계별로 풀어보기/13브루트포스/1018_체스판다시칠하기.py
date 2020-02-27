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

#####경은#####
# N, M = map(int, input().split())
# matrix = [list(map(str, input())) for _ in range(N)]
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == 'B':
#             matrix[i][j] = 0
#         else:
#             matrix[i][j] = 1
# repaint1 = [[0]*(M-7) for _ in range(N-7)]
# repaint2 = [[0]*(M-7) for _ in range(N-7)]
# for i in range(N-7):
#     for j in range(M-7):
#         for k in range(i, i+8):
#             for l in range(j, j+8):
#                 if ((k-i + l-j) % 2) and matrix[i][j] == matrix[k][l]:
#                     repaint1[i][j] += 1
#                 if ((k-i + l-j) % 2 == 0) and matrix[i][j] != matrix[k][l]:
#                     repaint1[i][j] += 1
# for i in range(N-7):
#     for j in range(M-7):
#         for k in range(i, i+8):
#             for l in range(j, j+8):
#                 if ((k-i + l-j) % 2) and not(matrix[i][j]) == matrix[k][l]:
#                     repaint2[i][j] += 1
#                 if ((k-i + l-j) % 2 == 0) and not(matrix[i][j]) != matrix[k][l]:
#                     repaint2[i][j] += 1
# minn = 64
# for i in range(N-7):
#     for j in range(M-7):
#         if repaint1[i][j] < minn:
#             minn = repaint1[i][j]
#         if repaint2[i][j] < minn:
#             minn = repaint2[i][j]
# print(minn)