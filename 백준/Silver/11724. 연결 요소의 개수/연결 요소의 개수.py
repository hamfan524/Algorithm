import sys
read = sys.stdin.readline
output = sys.stdout.write

def bfs(v):
  q = [v]
  while q:
    v = q.pop(0)
    for i in graph[v]:
      if visit_list[i] == 0:
        q.append(i)
        visit_list[i] = 1


n, m = map(int, read().split())
graph = [[] for i in range(n + 1)]

for i in range(m):
  a, b = map(int, read().split())
  graph[a].append(b)
  graph[b].append(a)

visit_list= [0] * (n + 1)
answer = 0

for i in range(1, n + 1):
  if visit_list[i] == 0:
    bfs(i)
    answer += 1

output(str(answer))