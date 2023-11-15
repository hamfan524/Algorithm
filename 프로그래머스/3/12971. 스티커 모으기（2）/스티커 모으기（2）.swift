func solution(_ sticker: [Int]) -> Int {
    let n = sticker.count
    
    if n == 1 {
        return sticker[0]
    }
    if n == 2 {
        return max(sticker[0], sticker[1])
    }
    
    var dp1 = [Int](repeating: 0, count: n - 1)
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    
    var dp2 = [Int](repeating: 0, count: n)
    dp2[0] = 0
    dp2[1] = sticker[1]
    dp2[2] = max(sticker[1], sticker[2])
    
    for i in 2..<n - 1 {
        dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])
        dp2[i + 1] = max(dp2[i - 1] + sticker[i + 1], dp2[i])
    }
    
    return max(dp1[n - 2], dp2[n - 1])
}
