N = int(input())
data_sort = []
cnt = 0
for _ in range(N):
    age, name = input().split()
    cnt += 1
    data_sort.append((int(age), cnt, name))
data_sort.sort()
for a, b, c in data_sort:
    print(a, c)