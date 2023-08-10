import heapq
N = int(input())
lecture = []
room = [0]
for _ in range(N):
    s, t = map(int, input().split())
    lecture.append((s, t))
lecture.sort()

for start, end in lecture:
    if start < room[0]:
        heapq.heappush(room, end)
    else:
        heapq.heappop(room)
        heapq.heappush(room, end)

print(len(room))