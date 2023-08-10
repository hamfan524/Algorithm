import sys
input = sys.stdin.readline
k = int(input())
answer = []
for _ in range(k):
    tmp = int(input())
    if tmp == 0:
        answer.pop()
    else:
        answer.append(tmp)
print(sum(answer))