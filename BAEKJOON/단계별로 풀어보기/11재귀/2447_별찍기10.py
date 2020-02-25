
def printstar(n):
    if not n:
        for s in range(len(star)):
            print(''.join(star[s]))
        return
    else:
        for l in range(0, N, n):
            for k in range(0, N, n):
                for i in range(n//3+l, 2*n//3+l):
                    for j in range(n//3+k, 2*n//3+k):
                        star[i][j] = ' '
        printstar(n//3)

N = int(input())
star = [['*']*N for _ in range(N)]
printstar(N)