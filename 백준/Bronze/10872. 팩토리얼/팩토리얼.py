import sys
input = sys.stdin.readline

dp = {
    0 : 1,
    1 : 1
}

def factorial(n):
  if n not in dp:
    dp[n] = n * factorial(n-1)
  return dp[n]


n = int(input())

print(factorial(n))