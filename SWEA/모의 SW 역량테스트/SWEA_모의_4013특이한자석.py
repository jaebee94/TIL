def rotate(n, d):
    if d == 1:
        tmp = mag[n][-1]
        mag[n] = mag[n][:7]
        mag[n].insert(0, tmp)
    elif d == -1:
        tmp = mag[n][0]
        mag[n] = mag[n][1:8]
        mag[n].append(tmp)


for T in range(int(input())):
    K = int(input())
    mag = [list(map(int, input().split())) for _ in range(4)]
    nd_list = [list(map(int, input().split())) for _ in range(K)]
    r = [0]*4
    score = 0
    for n, d in nd_list:
        n -= 1
        cnt = 0
        r[n] = d
        for i in range(n, 3):
            cnt += 1
            if mag[i][2] != mag[i+1][6]:
                if d == 1:
                    if not cnt//2:
                        r[i+1] = -1
                    else:
                        r[i+1] = 1
                elif d == -1:
                    if not cnt//2:
                        r[i+1] = 1
                    else:
                        r[i+1] = -1
            else:
                break
        cnt = 0
        for i in range(n, 0, -1):
            cnt += 1
            if mag[i][6] != mag[i-1][2]:
                if d == 1:
                    if not cnt//2:
                        r[i-1] = -1
                    else:
                        r[i-1] = 1
                else:
                    if not cnt//2:
                        r[i-1] = 1
                    else:
                        r[i-1] = -1
            else:
                break
        for m in range(4):
            rotate(m, r[m])
        r = [0]*4
    for i in range(4):
        if mag[i][0] == 1:
            score += 2**i
    print('#{} {}'.format(T+1, score))
