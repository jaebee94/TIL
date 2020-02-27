# 2108_통계학
###########시간초과###########
import sys

N = int(input())
num = [sys.stdin.readline() for _ in range(N)]
num_list = list(map(int, num))
# 산술평균
print(round(sum(num_list) / N))
# 중앙값
num_sort = sorted(num_list)
print(num_sort[N//2])
# 최빈값
maxx = ok = 0
for i in range(N):
    cnt = 0
    for j in range(i, N):
        if num_sort[i] == num_sort[j]:
            cnt += 1
    num_list[i] = cnt
    if cnt > maxx:
        maxx = cnt
for i in range(N):
    if num_list[i] == maxx:
        result = num_sort[i]
        ok += 1
    if ok == 2:
        result = num_sort[i]
        break
print(result)

# 범위        
print(num_sort[N-1] - num_sort[0])