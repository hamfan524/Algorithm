def dfs(depth, num):
    if depth == m:
        print(*tmp)
        return
    for i in range(num, n):
        if number[i] not in tmp:
            tmp.append(number[i])
            dfs(depth + 1, i)
            tmp.pop()
        
n, m = map(int, input().split())
number = list(map(int, input().split()))
tmp = []
number.sort()
dfs(0, 0)