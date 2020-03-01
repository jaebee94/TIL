def f(n, k, m):
    if n == k:
        print(' '.join(map(str, p)))
        return
    else:
        for i in range(m):
            if used[i] == 0:
                used[i] = 1
                p.append(start[i])
                f(n+1, k, m)
                p.pop()
            else:
                continue
            for j in range(i+1,N):
                used[j]=0


N, M = map(int, input().split())
used = [0] * N
p = []
start=[i+1 for i in range(N)]
f(0, M, N)