def cleaner(r, c, d):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    count = 0
    
    while True:
        if graph[r][c] == 0:
            graph[r][c] = 2
            count += 1
        
        for _ in range(4):
            nd = (d + 3) % 4
            nx = r + dx[nd]
            ny = c + dy[nd]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                r = nx
                c = ny
                d = nd
                break
            else:
                d = nd
        
        else:
            bd = (d + 2) % 4
            nx = r + dx[bd]
            ny = c + dy[bd]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != 1:
                r = nx
                c = ny
            else:
                return count

n, m = map(int, input().split())
r, c, d = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

print(cleaner(r, c, d))