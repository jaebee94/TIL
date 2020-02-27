N = int(input())
xy_list = []
for _ in range(N):
    x, y = map(int, input().split())
    xy_list.append((x, y))
xy_list.sort()
for i in range(N):
    print(' '.join(map(str, xy_list[i])))




#######시간초과########
# N = int(input())
# xy = [list(map(int, input().split())) for _ in range(N)]
# for i in range(N-1, 0, -1):
#     for j in range(i):
#         if xy[j][0] > xy[j+1][0]:
#             xy[j], xy[j+1] = xy[j+1], xy[j]
#         if xy[j][0] == xy[j+1][0] and xy[j][1] > xy[j+1][1]:
#             xy[j], xy[j+1] = xy[j+1], xy[j]
# for i in range(N):
#     print(' '.join(map(str, xy[i])))
