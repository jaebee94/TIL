def f(n, k, m):
    if n == k:
        print(' '.join(map(str, p)))
    else:
        for i in range(m):
            if used[i] == 0:
                used[i] = 1
                p[n] = i + 1
                f(n+1, k, m)
                used[i] = 0


N, M = map(int, input().split())
used = [0] * N
p = [0] * M
f(0, M, N)