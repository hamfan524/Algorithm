def solve():
    n = int(input())
    s = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    dp[0][0] = s[0][0]
    dp[1][0] = s[1][0]

    if n > 1:
        dp[0][1] = s[1][0] + s[0][1]
        dp[1][1] = s[0][0] + s[1][1]

    for i in range(2, n):
        dp[0][i] = s[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = s[1][i] + max(dp[0][i-1], dp[0][i-2])

    return max(dp[0][-1], dp[1][-1])

T = int(input())
for _ in range(T):
    print(solve())