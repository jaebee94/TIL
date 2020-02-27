N = int(input())
num_list = [int(input()) for _ in range(N)]

num = sorted(num_list)
for i in range(N):
    print(num[i])