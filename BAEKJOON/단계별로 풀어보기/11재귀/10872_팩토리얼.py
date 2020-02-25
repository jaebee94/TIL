# 재귀
def factorial(N):
    if N <= 1:
        return 1
    else:
        return N * factorial(N-1)

N = int(input())
print(factorial(N))

# for문
N = int(input())
result = 1
if N == 0:
    result = 0
else:
    for i in range(1, N+1):
        result *= i
print(result)