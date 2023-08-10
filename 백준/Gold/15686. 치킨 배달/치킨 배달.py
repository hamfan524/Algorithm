from itertools import combinations
import sys

def calDistance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(house, chickens):
    result = sys.maxsize
    for chicken in combinations(chickens, m):
        temp = 0
        for h in house:
            len = sys.maxsize
            for j in range(m):
                len = min(len, calDistance(h, chicken[j]))
            temp += len
        result = min(result, temp)
    return result

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
house = []
chickens = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            house.append([i, j])
        elif city[i][j] == 2:
            chickens.append([i, j])

print(solve(house, chickens))