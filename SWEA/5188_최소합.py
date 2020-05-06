di = [1, 0]
dj = [0, 1]
for tc in range(1, int(input())+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    i, j = 0, 0
    s = [(i, j, board[i][j])]
    minn = 13 * (2 * N - 1)
    while s:
        (i, j, n) = s.pop()
        for k in range(2):
            ni = i + di[k]
            nj = j + dj[k]
            if ni < N and nj < N:
                s.append((ni, nj, n + board[ni][nj]))
        if (i, j) == (N-1, N-1) and n < minn:
            minn = n
    print('#{} {}'.format(tc, minn))