def dfs(depth):
    if depth == m:
        print(*tmp)
        return
    for i in range(n):
        tmp.append(number[i])
        dfs(depth + 1)
        tmp.pop()

n, m = map(int, input().split())
number = list(map(int, input().split()))
tmp = []
number.sort()
dfs(0)