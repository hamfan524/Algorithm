def solution(n, words):
    answer = []
    tmp = []
    tmp.append(words[0])
    for i in range(1, len(words)):
        if words[i] in tmp:
            break
        else:
            if words[i][0] != words[i-1][-1]:
                break
        tmp.append(words[i])
    
    return [0, 0] if len(tmp) == len(words) else [(i % n) + 1, (i // n) + 1]