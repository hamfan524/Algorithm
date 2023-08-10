import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleep = [0  for _ in range(n + 3)]
check = [0  for _ in range(n + 3)]

for i in map(int, input().split()):
    sleep[i] = 1
for i in map(int, input().split()):
    if sleep[i] == 1:
        continue
    for j in range(i, n + 3, i):
        if sleep[j] != 1:
            check[j] = 1

for i in range(1, len(check)):
    check[i] += check[i-1]

for _ in range(m):
    s, e = map(int, input().split())
    print((e - s + 1) - check[e] + check[s - 1])