def solution(n, s):
    answer = []
    if s < n:
        return [-1]
    answer = [s // n for _ in range(n)]
    num = s % n
    i = 1
    while num:
        answer[n-i] += 1
        num -=1
        i += 1
    return answer 