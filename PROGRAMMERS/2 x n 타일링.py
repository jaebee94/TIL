def solution(n):
    f = [0, 1, 2]
    f += [0]*60000
    for i in range(3, n+1):
        f[i] = (f[i-1] + f[i-2]) % 1000000007
    return f[n]