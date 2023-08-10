from collections import deque

def check(x1, y1, x2, y2):
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    q = deque()
    count = 1
    q.append([x, y])
    graph[x][y] = 1
    visited[x][y] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and not visited[nx][ny]:
                count += 1
                visited[nx][ny] = True
                q.append([nx, ny])
    result.append(count)

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]
visited = [[False] * n for _ in range(m)]
result = []
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    check(x1, y1, x2, y2)

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i, j)

print(len(result))
result.sort()
print(*result)