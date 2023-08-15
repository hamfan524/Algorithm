def solution(msg):
    answer = []
    dic = {
        'A' : 1
    }
    for i in range(66, 91):
        dic[chr(i)] = dic[chr(i-1)] + 1
    idx = 27
    start, end = 0, 1
    
    while end <= len(msg):
        w = msg[start:end]
        if w in dic:
            end += 1
        else:
            dic[w] = idx
            idx += 1
            answer.append(dic[w[:-1]])
            start = end - 1
    answer.append(dic[w])
    
    return answer