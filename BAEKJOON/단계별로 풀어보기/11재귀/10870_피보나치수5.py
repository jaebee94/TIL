def fibo(N):
    if N == 0:
        return 0
    if N <= 2:
        return 1
    else:
        return fibo(N-1) + fibo(N-2)

N = int(input())
print(fibo(N))