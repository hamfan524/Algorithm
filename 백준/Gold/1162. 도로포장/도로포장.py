import sys
from heapq import heappush,heappop, heappushpop

input = sys.stdin.readline
inf = sys.maxsize

N, M, K = map(int, input().split())
K += 1
graph = [[] for _ in range(N)]
visit = [[False] * K for _ in range(N)]
dp =[[inf] * K for _ in range(N)]
heap = []

def dijkstra():
    heappush(heap, [0, 0, K - 1])

    for i in range(K):
        dp[0][i] = 0

    while heap:
        w, n, k = heappop(heap)

        if visit[n][k]:
            continue
        visit[n][k] = True
        for n_n, wei in graph[n]:
            if dp[n][k] + wei < dp[n_n][k]:
                dp[n_n][k] = dp[n][k] + wei
                heappush(heap, [dp[n_n][k] , n_n, k])
            if k > 0:
                if dp[n_n][k-1] > dp[n][k]:
                    dp[n_n][k-1] = dp[n][k]
                heappush(heap, [dp[n_n][k-1], n_n, k - 1])

for _ in range(M):
    c1, c2, t = map(int, input().split())
    graph[c1 - 1].append([c2 - 1, t])
    graph[c2 - 1].append([c1 - 1, t])

dijkstra()

print(min(dp[-1]))