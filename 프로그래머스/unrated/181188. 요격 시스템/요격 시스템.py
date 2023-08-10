def solution(targets):
    answer = 0
    targets.sort(key = lambda x: x[1])
    tmp = 0
    for target in targets:
        if tmp <= target[0]:
            answer += 1
            tmp = target[1]
    
    return answer