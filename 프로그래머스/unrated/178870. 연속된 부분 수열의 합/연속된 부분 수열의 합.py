def solution(sequence, k):
    answer = []
    count = len(sequence)
    tmp = sequence[0]
    idx = 0
    if k in sequence:
        return [sequence.index(k), sequence.index(k)]
    for i, j in enumerate(sequence):
        while tmp < k and idx <= len(sequence) - 2:
            idx += 1
            tmp += sequence[idx]
        if tmp == k and idx-i < count:
            count = idx-i
            answer = [i, idx]
        tmp -= j
        
    return answer