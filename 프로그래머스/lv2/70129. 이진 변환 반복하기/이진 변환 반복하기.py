def binary(num):
    result = ''
    while num > 1:
        result = str(num % 2) + result
        num //= 2
    result = str(num) + result
    return result

def solution(s):
    tmp = []
    loop = 0
    cnt = 0
    while True:
        loop += 1
        for i in s:
            if i == '0':
                cnt += 1
            else:
                tmp.append(i)
        s = binary(len(tmp))
        if s == '1':
            break
        tmp = []
        
    return [loop, cnt]