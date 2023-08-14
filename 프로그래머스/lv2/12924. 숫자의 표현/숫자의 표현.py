def solve(i, n):
    tmp = 0
    for j in range(i, n):
        tmp += j
        if tmp == n:
            return True
        elif tmp > n:
            return False
    
def solution(n):
    answer = 1
    
    for i in range(1, n):
        if solve(i, n):
            answer += 1   
        
    return answer