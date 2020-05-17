def DFS(y, sum):
    global result

    if y == N:
        if result > sum:
            result = sum
        return

    if result < sum:
        return

    for x in range(N):
        if not visited[x]:
            visited[x] = True
            DFS(y+1, sum + Data[y][x])
            visited[x] = False

TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    Data = [list(map(int, input().split())) for _ in range(N)]
    visited = [0]*N
    result = 100000000

    DFS(0, 0)
    print('#%d %d'%(tc, result))