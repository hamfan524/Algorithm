import sys
sys.setrecursionlimit(100000)

dp = {
    1 : 3,
    2 : 7
}

def f(n):
    if n not in dp:
        dp[n] = ((f(n-1) * 2) + f(n-2) ) % 9901
    return dp[n]

n = int(input())
print(f(n))