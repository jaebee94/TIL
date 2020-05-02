def solution(N):
    answer = [0, 1, 1]
    answer += [0]*80
    for i in range(3, N+2):
         answer[i] = answer[i-1] + answer[i-2]
    return 2 * (answer[N+1] + answer[N])