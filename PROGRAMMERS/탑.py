def solution(heights):
    answer = []
    for i in range(len(heights)-1, -1, -1):
        flag = 0
        for j in range(i-1, -1, -1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                flag = 1
                break
        if flag:
            continue
        answer.append(0)
    answer = answer[::-1]
            
    return answer