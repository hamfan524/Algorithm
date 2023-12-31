from collections import deque

def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    m = max(q)
    while True:
        a = q.popleft()
        if a == m:
            answer += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(q)
        else:
            q.append(a)
            if location == 0:
                location = len(q) - 1
            else:
                location -= 1

    return answer