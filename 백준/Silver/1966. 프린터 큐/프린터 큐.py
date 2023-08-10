import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    while q:
        tmp = q.popleft()
        if not q:
            print(cnt + 1)
            break
        
        if tmp < max(q):
            if m == 0:
                m += len(q)
            else:
                m -= 1
            q.append(tmp)
        else:
            if m == 0:
                print(cnt + 1)
                break
            else:
                cnt += 1
                m -= 1