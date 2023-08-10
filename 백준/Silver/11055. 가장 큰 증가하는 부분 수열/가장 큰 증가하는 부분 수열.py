import sys
input = sys.stdin.readline

n = int(input())
s = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(n):
  for j in range(i):
    if s[i] > s[j] and dp[i] < dp[j]:
      dp[i] = dp[j]      
  dp[i] += s[i]
  
print(max(dp))