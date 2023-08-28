from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sumQ1 = sum(queue1)
    sumQ2 = sum(queue2)
    limit = (len(queue1) + len(queue2)) * 2
    while queue1 and queue2:
        if answer > limit:
            return -1
        if sumQ1 == sumQ2:
            break
        if sumQ1 > sumQ2:
            tmp = queue1.popleft()
            sumQ1 -= tmp
            sumQ2 += tmp
            queue2.append(tmp)
            answer += 1
        else:
            tmp = queue2.popleft()
            sumQ2 -= tmp
            sumQ1 += tmp
            queue1.append(tmp)
            answer += 1
    if not queue1 or not queue2:
        return -1
    return answer