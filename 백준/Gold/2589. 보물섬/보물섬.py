from collections import deque

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    q = deque()
    q.append([x, y])
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    day = 0

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == "L" and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[cx][cy] + 1
                day = max(day, visited[nx][ny])

    return day - 1

n, m = map(int, input().split())
graph = [input() for _ in range(n)]
result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)