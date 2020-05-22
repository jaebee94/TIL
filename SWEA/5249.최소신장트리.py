def MST_PRIM(G):
    key = [float('inf') for _ in range(V + 1)]
    pi = [None for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]

    key[0] = 0
    for _ in range(V + 1):
        min_key = float('inf')
        start = -1
        for i in range(V + 1):
            if key[i] < min_key and not visited[i]:
                min_key = key[i]
                start = i
        visited[start] = True
        for next_v, next_w in G[start]:
            if next_w < key[next_v] and not visited[next_v]:
                key[next_v] = next_w
                pi[next_v] = start
    return sum(key)

for tc in range(1, int(input())+1):
    V, E = map(int, input().split())
    graph = {}
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        if n1 not in graph:
            graph[n1] = set()
        if n2 not in graph:
            graph[n2] = set()
        graph[n1].add((n2, w))
        graph[n2].add((n1, w))

    print('#{} {}'.format(tc, MST_PRIM(graph)))