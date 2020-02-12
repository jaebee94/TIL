# 1954. 달팽이 숫자

testcase = int(input())
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
for T in range(testcase):
    N = int(input())
    case = [[0]*N for _ in range(N)]
    i, j = 0, 0
    case[i][j] = 1
    cnt = 1
    flag = 0
    while 1:
        for k in range(4):
            while 1:
                if 0 > i+di[k] or i+di[k] >= N or 0 > j+dj[k] or j+dj[k] >= N or case[i+di[k]][j+dj[k]] != 0:
                    break
                i += di[k]
                j += dj[k]
                cnt += 1
                case[i][j] = cnt

            if case[i][j] == N ** 2:
                flag = 1
                break
        if flag:
            break

    print('#{}'.format(T+1))
    for n in range(N):
        print(' '.join(map(str, case[n])))

