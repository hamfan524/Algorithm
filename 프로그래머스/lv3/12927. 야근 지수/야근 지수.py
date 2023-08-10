from heapq import heappush, heappop
def solution(n, works):
    answer = 0
    heap = []
    for i in works:
        heappush(heap, -i)
    
    while n:
        tmp = heappop(heap)
        if tmp == 0:
            break
        n -= 1
        heappush(heap, tmp + 1)

    while heap:
        answer += heappop(heap) ** 2
    return answer

