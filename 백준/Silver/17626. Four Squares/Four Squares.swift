import Foundation

func solution(_ n: Int) -> Int{
    var dp: [Int] = [0, 1]
    var minNum: Int
    if n == 1 {
        return 1
    }
    for i in 2...n {
        minNum = Int.max
        for j in 1...Int(Double(i).squareRoot()) {
            minNum = min(minNum, dp[i-(j*j)] + 1)
        }
        dp.append(minNum)
    }
    
    return dp[n]
}

print(solution(Int(readLine()!)!))