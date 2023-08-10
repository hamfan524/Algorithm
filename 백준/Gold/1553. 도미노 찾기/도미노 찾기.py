dx = [0, 1]
dy = [1, 0]
def dfs(x, y):
    if x == 8: return 1
    cnt = 0
    nextX = x
    nextY = y + 1
    if nextY == 7:
        nextX = x + 1
        nextY = 0
    if visited[x][y]:
        return dfs(nextX, nextY)
    else:
        visited[x][y] = True
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(8) and ny in range(7) and not visited[nx][ny]:
                if not domino[graph[x][y]][graph[nx][ny]]:
                    domino[graph[x][y]][graph[nx][ny]] = domino[graph[nx][ny]][graph[x][y]] = True
                    visited[nx][ny] = True
                    cnt += dfs(nextX, nextY)
                    domino[graph[x][y]][graph[nx][ny]] = domino[graph[nx][ny]][graph[x][y]] = False
                    visited[nx][ny] = False
        visited[x][y] = False
        return cnt
    
graph = [list(map(int, list(input()))) for _ in range(8)]
visited = [[False] * 7 for _ in range(8)]
domino = [[False] * 7 for _ in range(7)]

print(dfs(0, 0))