from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    for i in course:
        c = []
        for order in orders:
            c += combinations(sorted(order), i)
        
        count = Counter(c)
        
        if len(count) != 0 and max(count.values()) > 1:
            answer += list(''.join(i) for i in count if count[i] == max(count.values()))

    return sorted(answer)
