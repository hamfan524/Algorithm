from collections import defaultdict
def solution(clothes):
    dd = defaultdict(int)
    for i in clothes:
        dd[i[1]] += 1      
    answer = 1
    for i in dd.values():
        answer *= (i + 1)
           
    return answer - 1