from collections import deque

def solution(s):

    q = deque()
    
    if s[0] == ')':
        return False
    q.append(s[0])

    for i in range(1, len(s)):
        if s[i] == '(':
            q.append(s[i])
        else:
            if len(q) == 0:
                return False
            tmp = q.pop()
    
    return True if len(q) == 0 else False