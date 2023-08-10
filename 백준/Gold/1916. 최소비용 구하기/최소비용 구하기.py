import sys
from heapq import heappush, heappop

input = sys.stdin.readline
inf = sys.maxsize

def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if fixed[n] or dp[n] == inf:
            continue
        fixed[n] = True
        for n_n, wei in graph[n]:
            n_w = wei + w
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
dp = [inf] * (n + 1)
fixed = [False] * (n + 1)
heap = []

for _ in range(m):
    d, a, v = map(int, input().split())
    graph[d].append([a, v])

d_c, a_c = map(int, input().split())

dijkstra(d_c)
print(dp[a_c])