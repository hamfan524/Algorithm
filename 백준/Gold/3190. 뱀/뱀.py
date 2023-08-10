from collections import deque
import sys
input = sys.stdin.readline

def turn(change):
    global nd
    if change == 'D':
        nd = (nd + 1) % 4
    else:
        nd = (nd - 1) % 4

n = int(input())
graph = [[0] * n for _ in range(n)]
k = int(input())
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
oper = dict()
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

l = int(input())
for _ in range(l):
    s, d = input().split()
    oper[int(s)] = d

x, y = 0, 0
graph[x][y] = 2
cnt = 0
nd = 0
q = deque()
q.append([0, 0])

while True:
    cnt += 1
    x += directions[nd][0]
    y += directions[nd][1]
    if x not in range(n) or y not in range(n):
        break
    if graph[x][y] == 1:
        graph[x][y] = 2
        q.append([x, y])
        if cnt in oper:
            turn(oper[cnt])

    elif graph[x][y] == 0:
        graph[x][y] = 2
        q.append([x, y])
        px, py = q.popleft()
        graph[px][py] = 0
        if cnt in oper:
            turn(oper[cnt])
    else:
        break

print(cnt)