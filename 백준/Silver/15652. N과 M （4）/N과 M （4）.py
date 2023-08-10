def dfs(depth, num):
    if depth == m:
        print(*tmp)
        return
    for i in range(num, n + 1):
        tmp.append(i)
        dfs(depth + 1, i)
        tmp.pop()

n, m = map(int, input().split())
tmp = []
dfs(0, 1)