def solution(arr):
    answer = 1
    for i in arr:
        answer = (answer * i) / lcs(answer, i)
    return answer

def lcs(n, m):
    if n % m == 0: return m
    else: return lcs(m, (n % m))
