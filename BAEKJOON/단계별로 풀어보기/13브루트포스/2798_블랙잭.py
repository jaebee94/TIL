N, M = map(int, input().split())
cards = list(map(int, input().split()))
maxx = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            summ = cards[i] + cards[j] + cards[k]
            if summ <= M and summ > maxx:
                maxx = summ
print(maxx)