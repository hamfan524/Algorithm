def dfs(depth, num):
    if depth == m:
        if tuple(tmp) not in result:
            print(*tmp)
            result.add(tuple(tmp))
        return
    for i in range(num, n):
        if i not in stack:
            stack.append(i)
            tmp.append(number[i])
            dfs(depth + 1, i)
            stack.pop()
            tmp.pop()

n, m = map(int, input().split())
number = list(map(int, input().split()))
number.sort()
stack = []
tmp = []
result = set()
dfs(0, 0)