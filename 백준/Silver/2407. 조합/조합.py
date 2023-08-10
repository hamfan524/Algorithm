def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num

def combi(n, m):
    return factorial(n) // (factorial(n - m) * factorial(m))

n, m = map(int, input().split())
print(combi(n, m))