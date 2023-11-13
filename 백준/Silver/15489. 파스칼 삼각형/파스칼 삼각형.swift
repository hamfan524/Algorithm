func solution(_ r: Int, _ c: Int, _ w: Int) -> Int {
    var dp = [[Int]](repeating: [Int](repeating: 0, count: 30), count: 30)
    dp[0][0] = 1
    
    for i in 0...29 {
        for j in 0...i {
            if i == 0 || j == 0 || j == i {
                dp[i][j] = 1
            } else {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            }
        }
    }
    var total = 0
    for i in (r-1)..<(r+w-1) {
        for j in (c-1)..<(c + i - r + 1) {
            total += dp[i][j]
        }
    }
    return total
}

let input = readLine()!.split(separator: " ").map { Int($0)! }

let r = input[0]
let c = input[1]
let w = input[2]

print(solution(r, c, w))