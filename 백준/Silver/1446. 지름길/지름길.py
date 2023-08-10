from heapq import heappush,heappop
import sys

def dijkstra(start):
    dp[start] = 0
    heap = []
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if w > dp[n]:
            continue
        for n_n, wei in graph[n]:
            n_w = w + wei
            if n_w < dp[n_n]:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])

    return dp[-1]

n, d = map(int, input().split())
graph = [[] for _ in range(d + 1)]
dp = [sys.maxsize] * (d + 1)

for i in range(d):
    graph[i].append([i + 1, 1])

for _ in range(n):
    start, end, length = map(int, input().split())
    if end > d:
        continue
    graph[start].append([end, length])

print(dijkstra(0))