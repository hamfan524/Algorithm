import sys
read = sys.stdin.readline

def fibonacci(n):
  if n > 1:
    return fibonacci(n-2) + fibonacci(n-1)
  else:
    return n 


n = int(read())

print(fibonacci(n))