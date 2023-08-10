def dfs(depth):
    if depth == m:
        if tuple(tmp) not in result:
            print(*tuple(tmp))
            result.add(tuple(tmp))
        return
    for i in range(n):
        if i in stack:
            continue
        tmp.append(numbers[i])
        stack.append(i)
        dfs(depth + 1)
        tmp.pop()
        stack.pop()

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
stack = []
tmp = []
result = set()
numbers.sort()
dfs(0)