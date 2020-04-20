def solution(prices):
    answer = []
    for i in range(len(prices)):
        t = 0
        for j in range(i+1, len(prices)):
            t += 1
            if prices[i] > prices[j]:
                break
        answer.append(t)
    return answer