N, M = map(int, input().split())
num = int(input())
x = [0]
y = [0]
for _ in range(num):
    d, a = map(int, input().split())
    if d:
        y.append(a)
    else:
        x.append(a)
x.sort()
x.append(M)
y.sort()
y.append(N)
maxx = 0
for i in range(1, len(x)):
    for j in range(1, len(y)):
        p = x[i] - x[i-1]
        q = y[j] - y[j-1]
        area = p * q
        if area > maxx:
            maxx = area
print(maxx)
