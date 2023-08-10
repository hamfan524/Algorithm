def dfs(x, y, tmp, cnt):
    global maxValue, dx, dy
    if cnt == 4:
        maxValue = max(maxValue, tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, tmp + graph[nx][ny], cnt + 1)
            visited[nx][ny] = False

def checkFuck(x, y):
    global maxValue, dx, dy
    value = graph[x][y]
    tmp = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            tmp.append(graph[nx][ny])
    if len(tmp) == 4:
        tmp.remove(min(tmp))
    value += sum(tmp)
    maxValue = max(maxValue, value)

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

maxValue = 0
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, graph[i][j], 1)
        visited[i][j] = False
        checkFuck(i, j)
print(maxValue)