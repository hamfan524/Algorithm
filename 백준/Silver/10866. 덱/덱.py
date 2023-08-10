from collections import deque
import sys

input = sys.stdin.readline
q = deque()
for _ in range(int(input())):
    tmp = input().split()
    if tmp[0] == 'push_front':
        q.appendleft(tmp[1])
    elif tmp[0] == 'push_back':
        q.append(tmp[1])
    elif tmp[0] == 'pop_front':
        print(q.popleft()) if len(q) else print(-1)
    elif tmp[0] == 'pop_back':
        print(q.pop()) if len(q) else print(-1)
    elif tmp[0] == 'size':
        print(len(q))
    elif tmp[0] == 'empty':
        print(0) if len(q) else print(1)
    elif tmp[0] == 'front':
        print(q[0]) if len(q) else print(-1)
    else:
        print(q[-1]) if len(q) else print(-1)