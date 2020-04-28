def cal(a, b):
    result = [a+b, a-b, a*b, b+a, b-a, b*a]
    if b:
        result.append(a//b)
    if a:
        result.append(b//a)
    result = set(result)
    return result

def solution(N, number):
    if N == number:
        return 1
    dp = [0, [N]]
    for i in range(2, 9):
        tmp = [int(str(N)*i)]
        for j in range(1, i//2+1):
            for a in dp[j]:
                for b in dp[i-j]:
                    tmp += cal(a, b)
        if number in tmp:
            return i
        else:
            dp.append(tmp)
    return -1