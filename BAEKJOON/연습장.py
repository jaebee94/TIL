def dfs(ni,nj):
    global cnt, e, memo
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, 0, -1, 1]
    visited.append([ni,nj])
    cnt += memo
    e += 1
    for k in range(8):
        if 0 <= ni+dx[k] < N:
            if 0 <= nj+dy[k] < N:
                if mapp[ni+dx[k]][nj+dy[k]] == memo:
                    if [ni+dx[k],nj+dy[k]] not in visited:
                        ni = ni+dx[k]
                        nj = nj+dy[k]
                        dfs(ni,nj)

T = int(input())
for t in range(1,T+1):
    N =int(input())
    mapp= [list(map(int,input().split())) for _ in range(N)]
    visited = []
    cntresult = []
    eresult = []
    for i in range(N):
        for j in range(N):
            e = 0
            cnt = 0
            if [i,j] not in visited:
                if mapp[i][j] !=0:
                    memo = mapp[i][j]
                    ni = i
                    nj = j
                    dfs(ni,nj)
                    cntresult.append(cnt)
                    eresult.append(e)
    maxx = max(cntresult)
    minn = 400
    for i in range(len(eresult)):
        if cntresult[i] == maxx:
            if eresult[i] <= minn:
                minn = eresult[i]
    print(cntresult)
    print("#{} {} {}".format(t,maxx,minn))




