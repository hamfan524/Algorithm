def solution(operations):
    import heapq
    from collections import deque

    heap = []
    operations = deque(operations)
    while operations:
    
        temp = operations.popleft()
        if temp[0] == "I":
            heapq.heappush(heap, int(temp[2:]))
        elif heap:
            if temp[2] == "1":
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)

    if heap:
        answer = [max(heap), heapq.heappop(heap)]
    else:
        answer = [0, 0]
    return answer