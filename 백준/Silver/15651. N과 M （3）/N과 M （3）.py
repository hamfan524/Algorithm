def dfs(depth):
    if depth == m:
        print(*tmp)
        return
    for i in range(1, n + 1):
        tmp.append(i)
        dfs(depth + 1)
        tmp.pop()

n, m = map(int, input().split())
tmp = []
dfs(0)