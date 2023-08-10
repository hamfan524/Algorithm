def solution(s):
    answer = []
    for i in range(1, len(s)//2 + 2):
        answer.append(compress(s, i))
    return min(answer)

def compress(s, n):
    compression= ['']
    num = 0

    a = [s[i : i + n]for i in range(0, len(s), n)]
    
    for i in a:
        if compression[-1] != i:
            if num > 1:
                compression.append(str(num))
            compression.append(i)
            num = 0
        if compression[-1] == i:
            num += 1
    if num > 1:
        compression.append(str(num))

    return len(''.join(compression))