def check(cs):
    for _ in range(len(cs)):
        cs = cs.replace('[]', '')
        cs = cs.replace('()', '')
        cs = cs.replace('{}', '')
        
    return True if not len(cs) else False

def solution(s):
    answer = 0

    for i in range(len(s)):
        if check(s):
            answer += 1
        s = s[1:] + s[0]

    return answer