def is_available(candidate, col):
    row = len(candidate)
    for i in range(row):
        if candidate[i] == col or candidate[i] - col == row - i or candidate[i] - col == i - row:
            return False
    return True

def dfs(N, row, candidate, result):
    if row == N:
        result.append(candidate[:])
        return
    for i in range(N):
        if is_available(candidate, i):
            candidate.append(i)
            dfs(N, row + 1, candidate, result)
            candidate.pop()

def solve(N):
    result = []
    dfs(N, 0, [], result)
    return len(result)

N = int(input())
print(solve(N))