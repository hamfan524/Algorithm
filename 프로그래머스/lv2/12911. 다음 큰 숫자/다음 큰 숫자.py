def count(n):
    result = ''
    while n > 1:
        result = str(n % 2) + result
        n //= 2 
    result = str(n) + result
    return result.count('1')

def solution(n):
    answer = 0
    tmp = count(n)
    while True:
        n += 1
        if tmp == count(n):
            answer = n
            break
    return answer