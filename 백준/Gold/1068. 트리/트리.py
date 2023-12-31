import sys
input = sys.stdin.readline

n = int(input())
parents = list(map(int, input().split()))
del_node = int(input())
tree = {}

for i in range(n):
  if i == del_node or parents[i] == del_node:
    continue
  if parents[i] in tree:
    tree[parents[i]].append(i)
  else:
    tree[parents[i]] = [i]
    
res = 0
if -1 in tree:
  q = [-1]
else:
  q = []
while q:
  node = q.pop()
  if node not in tree:
    res += 1
  else:
    q += tree[node]

print(res)