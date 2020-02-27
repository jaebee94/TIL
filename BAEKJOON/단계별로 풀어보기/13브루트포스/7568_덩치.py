N = int(input())
spec = []
for _ in range(N):
    elem = list(map(int, input().split()))
    spec.append(elem)
for n in range(N):
    cnt = 1
    for i in range(N):
        if spec[n][0] < spec[i][0] and spec[n][1] < spec[i][1]:
            cnt += 1
    print(cnt, end=' ')