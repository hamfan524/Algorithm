n = int(input())
graph = [[0] * 101 for _ in range(101)]
answer = 0
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x-10, x):
        for j in range(y-10, y):
            graph[i][j] = 1
for i in graph:
    answer += i.count(1)
print(answer)