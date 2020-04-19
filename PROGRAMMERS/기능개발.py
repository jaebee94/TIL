def solution(progresses, speeds):
    answer = []
    days = []
    for i in range(len(progresses)):
        day = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            day += 1
        days.append(day)
    days.append(100)
    cnt = 1
    max_day = days[0]
    for i in range(len(days)-1):
        if max_day >= days[i+1]:
            cnt += 1
        else:
            answer.append(cnt)
            max_day = days[i+1]
            cnt = 1
    return answer