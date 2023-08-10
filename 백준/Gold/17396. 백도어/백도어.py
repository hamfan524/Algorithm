from heapq import heappush, heappop
import sys

inf = sys.maxsize

n, m = map(int, input().split())
N = list(map(int, input().split()[:n]))
N[-1] = 0
graph = [[] for _ in range(n + 1)]
dp = [inf for _ in range(n)]
heap = []

for _ in range(m):
    a, b, t = map(int, input().split())
    graph[a].append([b, t])
    graph[b].append([a, t])

def dijkstra(start):
    dp[start] = 0
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if w > dp[n]:
            continue
        for n_n, wei in graph[n]:
            n_w = w + wei
            if n_w < dp[n_n] and N[n_n] == 0:
                dp[n_n] = n_w
                heappush(heap, [n_w, n_n])
    return dp[-1] if dp[-1] != inf else -1

print(dijkstra(0))