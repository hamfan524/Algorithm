def dfs(depth):
    if depth == m:
        if tuple(tmp) not in result:
            print(*tmp)
            result.add(tuple(tmp))
        return
    for i in range(n):
        tmp.append(number[i])
        dfs(depth + 1)
        tmp.pop()

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
tmp = []
result = set()
dfs(0)