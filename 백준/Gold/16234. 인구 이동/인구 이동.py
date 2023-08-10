from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    temp = []
    q = deque()

    temp.append([x, y])
    q.append([x, y])
    visited[x][y] = True
    totalPopulation = graph[x][y]
    count = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == False:
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r:
                    q.append([nx, ny])
                    visited[nx][ny] = True
                    temp.append([nx, ny])
                    totalPopulation += graph[nx][ny]
                    count += 1

    for i, j in temp:
        graph[i][j] = totalPopulation // count

    return count                    


n, l, r = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

result = 0

while True:
    visited = [[False] * n for _ in range(n)]
    moved = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    moved = True
    if not moved:
        break
    result += 1

print(result)