import sys

N = int(input())
num = [sys.stdin.readline() for _ in range(N)]
num = map(int, num)
a = sorted(num)
for i in range(N):
    print(a[i])



# import sys

# N = int(input())
# num = [sys.stdin.readline() for _ in range(N)]
# a = list(map(int, num))
# for i in range(N, 0, -1):
#     for j in range(0, i-1):
#         if a[j] > a[j+1]:
#             a[j], a[j+1] = a[j+1], a[j]
# for i in range(N):
#     print(a[i])
