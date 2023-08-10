import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    tmp = list(input().split())
    if tmp[0] == 'add':
        s.add(tmp[1])
    elif tmp[0] == 'remove':
        s.discard(tmp[1])
    elif tmp[0] == 'check':
        print(1) if tmp[1] in s else print(0)
    elif tmp[0] == 'toggle':
        s.add(tmp[1]) if tmp[1] not in s else s.discard(tmp[1])
    elif tmp[0] == 'all':
        s = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'}
    else:
        s.clear()