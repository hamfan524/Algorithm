from collections import defaultdict

def solution(numbers, target):
    a = [0]
    answer = defaultdict(int)
    answer[0] = 1
    for n in numbers:
        dp = defaultdict(int)
        tmp = []
        for i in a:
            if i+n not in dp:
                tmp.append(i+n)
            if i-n not in dp:
                tmp.append(i-n)
            dp[i+n] += answer[i]
            dp[i-n] += answer[i]
        answer = dp
        a = tmp
    return answer[target]

