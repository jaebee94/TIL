N = int(input())
xy_sort = []
for _ in range(N):
    x, y = map(int, input().split())
    xy_sort.append((y, x))
xy_sort.sort()
for y, x in xy_sort:
    print(x, y)