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

#####경은#####
import sys
N = int(sys.stdin.readline())
n = N//10
while n < N:
    gen = list(map(int, str(n)))
    total = sum(gen) + n
    if total == N:
        result = ''.join(map(str, gen))
        break
    n += 1
    if n== N:
        result = 0
        break
print(result)