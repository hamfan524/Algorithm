import sys
def solution(x, y, n):
    inf = sys.maxsize
    dp = [inf] * (y + 1)
    num = [i for i in range(y+1)]
    dp[x] = 0
    for i in range(x+1, y+1):
        if i % 2 == 0 and i % 3 == 0:
            dp[i] = min(dp[i-n], dp[i // 2], dp[i // 3]) + 1
        elif i % 3 == 0:
            dp[i] = min(dp[i-n], dp[i // 3]) + 1
        elif i % 2 == 0:
            dp[i] = min(dp[i-n], dp[i // 2]) + 1
        elif i - n >= 0:
                dp[i] = dp[i - n] + 1

    return dp[-1] if dp[-1] < 1000000 else -1