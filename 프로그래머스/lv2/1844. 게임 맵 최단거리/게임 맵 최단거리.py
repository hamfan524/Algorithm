from collections import deque


def bfs(x, y, maps, visited):
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]
    
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < len(maps)  and 0 <= ny < len(maps[0]) and maps[nx][ny] == 1 and visited[nx][ny] == 0:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    
def solution(maps):
    answer = 0
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]
    bfs(0, 0, maps, visited)
    print(visited)

    return visited[-1][-1] if visited[-1][-1] != 0 else -1