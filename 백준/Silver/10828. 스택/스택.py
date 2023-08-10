import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    tmp = list(input().split())
    if tmp[0] == 'pop':
        print(stack.pop()) if len(stack) else print(-1)
    elif tmp[0] == 'size':
        print(len(stack))
    elif tmp[0] == 'empty':
        print(0) if len(stack) else print(1)
    elif tmp[0] == 'top':
        print(stack[-1]) if len(stack) else print(-1)
    else:
        stack.append(tmp[1])