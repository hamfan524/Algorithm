import sys
input = sys.stdin.readline

n = int(input())
sheet = list(map(int, input().split()))
fault = [0 for _ in range(n)]
for i in range(1, n):
    if sheet[i] < sheet[i-1]:
        fault[i] = 1

for i in range(1, n):
    fault[i] += fault[i-1]

q = int(input())
for _ in range(q):
    x, y = map(int, input().split())
    print(fault[y-1] - fault[x-1])
