N = int(input())
for n in range(N):
    numbers = [n]
    numbers = list(str(n))
    numbers.append(n)
    if sum(map(int, numbers)) == N:
        result = n
        break
    result = 0
print(result)