def dfs(depth):
    if depth == m:
        print(' '.join(map(str, tmp)))
        return
    for i in range(n):
        if numbers[i] in tmp:
            continue
        tmp.append(numbers[i])
        dfs(depth + 1)
        tmp.pop()

n, m = map(int, input().split())
tmp = []
numbers = list(map(int, input().split()))
numbers.sort()

dfs(0)