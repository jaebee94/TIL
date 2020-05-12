def bfs(vector, visited, start):
    answer = 0
    visited[start] = True
    q = []
    for value in vector[start]:
        q.append(value)
        visited[value] = True
    while len(q) !=0 :
        loop = len(q)
        for i in range(loop):
            curnode = q.pop(0)
            for value in vector[curnode]:
                if visited[value] == False:
                    visited[value] = True
                    q.append(value)
        answer = loop
    return answer

def solution(n, vertex):
    answer = 0
    visited = [False for _ in range(20001)]
    vector = [[] for i in range(20001)]
    for value in vertex:
        node1= value[0]
        node2= value[1]
        vector[node1].append(node2)
        vector[node2].append(node1)
    answer = bfs(vector,visited ,1)
    return answer