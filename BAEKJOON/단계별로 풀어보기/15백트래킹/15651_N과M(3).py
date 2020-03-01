def f(n, k, m):
    if n == k:
        print(' '.join(map(str, p)))
    else:
        for i in range(m):
            p[n] = i + 1
            f(n+1, k, m)


N, M = map(int, input().split())
p = [0] * M
f(0, M, N)