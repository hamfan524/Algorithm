def solution(s):
    answer = []
    t = s[2:-2].split('},{')
    t.sort(key = len)
    for i in t:
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    return answer

