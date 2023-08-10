
def solution(n):
    answer = []

    def hanoi(left, m, right, n):
        if n == 1:
            answer.append([left, right])
        else:
            hanoi(left, right, m, n - 1)
            hanoi(left, m, right, 1)
            hanoi(m, left, right, n - 1)
            
    hanoi(1, 2, 3, n)
    
    return answer