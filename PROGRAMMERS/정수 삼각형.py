def solution(triangle):
    for i in range(len(triangle)):
        if i == 0: continue
        for j in range(len(triangle[i])):
            if j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][-1]
            elif j == 0:
                triangle[i][j] += triangle[i-1][0]
            else:
                if triangle[i][j] + triangle[i-1][j-1] >= triangle[i][j] + triangle[i-1][j]:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += triangle[i-1][j]
    answer = max(triangle[-1])
    return answer