def solution(budgets, M):
    if sum(budgets) <= M:
        return max(budgets)
    
    budgets.sort()
    l = len(budgets)
    start, end = 0, l - 1
    while start <= end:
        mid = (start + end) // 2
        req_sum = sum(budgets[0:mid]) + budgets[mid]*(l-mid)
        if req_sum >= M:
            end = mid - 1
        else:
            start = mid + 1
            
    for i in range(mid, l):
        summ = sum(budgets[0:i]) + budgets[i]*(l-i)
        if summ >= M:
            while summ >= M:
                budgets[i] -= 1
                summ = sum(budgets[0:i]) + budgets[i]*(l-i)
            return budgets[i]