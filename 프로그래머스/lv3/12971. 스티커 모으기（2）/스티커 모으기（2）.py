def solution(sticker):
    answer = 0
    if len(sticker) == 1:
        return sticker[0]
    if len(sticker) == 2:
        return max(sticker[0], sticker[1])
    dp = [0 for _ in range(len(sticker)-1)]
    dp_ = [0 for _ in range(len(sticker))]
    dp[0] = sticker[0]    
    dp[1] = max(dp[0], sticker[1])
    dp_[1] = sticker[1]
    dp_[2] = max(dp_[1], sticker[2])
    
    for i in range(2, len(sticker)-1):
        dp[i] = max(dp[i-2] + sticker[i], dp[i-1])
    for i in range(3, len(sticker)):
        dp_[i] = max(dp_[i-2] + sticker[i], dp_[i-1])
                
    return max(dp[-1], dp_[-1])