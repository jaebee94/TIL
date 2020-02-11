# 오목

N = int(input())
# 바둑판
board = [[0]*19 for _ in range(19)]
dx = [0, 1, 1, 1]
dy = [1, 1, 0, -1]
flag = 0
for n in range(N):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    # 흑 : 1, 백 : 2
    if not n % 2:
        board[x][y] = color = 1
    else:
        board[x][y] = color = 2

    for k in range(4):
        cnt = 1
        x1 = x + dx[k]
        y1 = y + dy[k]
        x2 = x - dx[k]
        y2 = y - dy[k]
        while 0 <= x1 < 19 and 0 <= y1 < 19 and board[x1][y1] == color:
            cnt += 1
            x1 = x1 + dx[k]
            y1 = y1 + dy[k]

        while 0 <= x2 < 19 and 0 <= y2 < 19 and board[x2][y2] == color:
            cnt += 1
            x2 = x2 - dx[k]
            y2 = y2 - dy[k]
        if cnt == 5:
            flag = 1
            break
    if flag:
        print(n + 1)
        break
if not flag:
    print(-1)