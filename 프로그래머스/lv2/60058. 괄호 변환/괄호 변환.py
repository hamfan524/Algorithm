def div(p):
    check = 0
    for i in range(len(p)):
        if p[i] == '(':
            check -= 1
        else:
            check += 1
        if check == 0:
            return p[:i + 1], p[i + 1:]
        
def check(u):
    tmp = []
    for i in u:
        if i == '(':
            tmp.append(i)
        else:
            if len(tmp) == 0:
                return False
            else:
                tmp.pop()
    return True

def solution(p):
    if not p:
        return p
    u, v = div(p)
    print(u, v)
    if check(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) +')'
        for i in u[1:-1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
    return answer