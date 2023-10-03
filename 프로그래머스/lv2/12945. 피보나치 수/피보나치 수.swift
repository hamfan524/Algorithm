import Foundation

var dp: [Int: Int] = [
    0: 0,
    1: 1,
    2: 1
]

func solution(_ n: Int) -> Int {
    let answer = fibo(n)
    return answer % 1234567
}

func fibo(_ n: Int) -> Int {
    if dp[n] == nil {
        dp[n] = (fibo(n - 1) + fibo(n - 2)) % 1234567
    }
    return dp[n]!
}