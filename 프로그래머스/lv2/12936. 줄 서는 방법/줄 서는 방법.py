from math import factorial
def solution(n, k):
    answer = [i for i in range(1, n + 1)]
    stack = []
    k -= 1
    while answer:
        a = k // factorial(n - 1)
        stack.append(answer[a])
        del answer[a]
        
        k = k % factorial(n - 1)
        n -= 1
    return stack
 