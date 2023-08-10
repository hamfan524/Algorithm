import sys
from collections import deque
input = sys.stdin.readline
inf = sys.maxsize

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
def bfs(x, y):
    q = deque()
    graph[x][y] = 0
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    q.append((x, y, 1))
    dist = inf
    cand = []
    while q:
        xx, yy, cCnt = q.popleft()
        if cCnt > dist:
            return min(cand)
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if nx in range(n) and ny in range(n) and not visited[nx][ny]:
                if graph[nx][ny] != 0 and graph[nx][ny] < size:
                    cand.append([nx, ny, cCnt])
                    dist = min(dist, cCnt)
                if graph[nx][ny] <= size:
                    visited[nx][ny] = True
                    q.append((nx, ny, cCnt + 1))
    return min(cand) if cand else (-1, -1, -1)
           
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
size = 2
eatCnt = 0
sx, sy = 0, 0
cnt = 0

# 상어 위치
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            sx, sy = i, j
            
while True:
    fish_pos = bfs(sx, sy)

    if fish_pos[0] == -1:
        print(cnt)
        exit()
    graph[fish_pos[0]][fish_pos[1]] = 9
    cnt += fish_pos[2]
    eatCnt += 1
    if eatCnt == size:
        eatCnt, size = 0, size + 1
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                sx, sy = i, j