def solution(n):
    answer = [0]
    cnt = 1
    while cnt < n:
        cnt += 1
        reverse = [0]*len(answer)
        for i in range(len(answer)):
            if answer[i] == 0:
                reverse[-1-i] = 1
        answer += [0] + reverse
    return answer