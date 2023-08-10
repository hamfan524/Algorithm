from collections import deque

def bfs(x, y, maps, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    count = 0
    visited[x][y] = True
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        count += int(maps[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != 'X' and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = True

    return count

def solution(maps):
    visited = [[False] * len(maps[i]) for i in range(len(maps))]
    result = []
    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if maps[i][j] != 'X' and not visited[i][j]:
                result.append(bfs(i, j, maps, visited))

    return sorted(result) if len(result) != 0 else [-1]