import sys
sys.setrecursionlimit(10**7)

dp = {
    0 : 0,
    1 : 1,
    2 : 1
}
def solution(n):
    answer = fibo(n)
    return answer %1234567

def fibo(n):
    if n not in dp:
        dp[n] = fibo(n-1) + fibo(n-2)
    return dp[n]