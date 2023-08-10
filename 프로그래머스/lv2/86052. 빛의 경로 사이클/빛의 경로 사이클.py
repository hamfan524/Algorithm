def move(x, y, dx, dy):
    return (x + dx) % n, (y + dy) % m

def solution(grid):
    answer = []
    global n, m
    n, m = len(grid), len(grid[0])
    visited = [[[False] * 4 for _ in range(m)] for _ in range(n)]
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    for i in range(n):
        for j in range(m):
            for k in range(4):
                if not visited[i][j][k]:
                    x, y, d = i, j, k
                    cnt = 0
                    while not visited[x][y][d]:
                        visited[x][y][d] = True
                        cnt += 1
                        x, y = move(x, y, dx[d], dy[d])
                        if grid[x][y] == 'R':
                            d = (d + 1) % 4
                        if grid[x][y] == 'L':
                            d = (d - 1) % 4
                    answer.append(cnt)
    answer.sort()
    return answer