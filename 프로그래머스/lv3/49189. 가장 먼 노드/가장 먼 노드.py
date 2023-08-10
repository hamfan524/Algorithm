from collections import deque

def bfs(graph, visited):
    q = deque()
    q.append(1)
    visited[1] = 1
    while q:
        n = q.popleft()
        for g in graph[n]:
            if visited[g] == 0:
                q.append(g)
                visited[g] = visited[n] + 1

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    visited = [0] * (n + 1)

    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    bfs(graph, visited)

    max_edge = max(visited)
    for i in visited:
        if i == max_edge:
            answer += 1

    return answer