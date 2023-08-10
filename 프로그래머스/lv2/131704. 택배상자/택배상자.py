from collections import deque

def solution(order):
    answer = 0
    container = deque(i for i in range(1, len(order) + 1))
    subContain = []
    i = 0

    while i < len(order):
        change = False
        if container and order[i] > container[0]:    
            subContain.append(container.popleft())
            change = True
        if container and container[0] == order[i]:
            answer += 1
            container.popleft()
            i += 1
            change = True
        if subContain and subContain[-1] == order[i]:
            answer += 1
            subContain.pop()
            i += 1
            change = True
        if change == False:
            break
        
    return answer