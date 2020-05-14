def dfs(cur, tickets, visited):
    if len(tickets) == 0:
        return visited
    for i, ticket in enumerate(tickets):
        if cur == ticket[0]:
            arrival = ticket[1]
            visited.append(arrival)
            tickets.pop(i)
            result = dfs(arrival, tickets, visited)
            if len(result) != 0:
                 return result
            visited.pop()
            tickets.insert(i, [cur, arrival])
    return []

def solution(tickets):
    tickets.sort()
    visited = ["ICN"]
    cur = "ICN"
    answer = dfs(cur, tickets, visited)
    return answer