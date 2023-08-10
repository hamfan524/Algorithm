n = int(input())
number = list(map(int, input().split()))
dp = [number[0]]
for i in range(1, n):
    dp.append(dp[i-1] + number[i])

sum = 0
for i in range(n):
    sum += number[i] * (dp[n-1] - dp[i])

print(sum)