from collections import defaultdict

def solution(k, tangerine):
    dd = defaultdict(int)
    for i in tangerine:
        dd[i] += 1

    dd = sorted(dd.values(), reverse = True)

    answer = 0
    for i in range(len(dd)):
        answer += 1
        k -= dd[i]
        if k <= 0:
            break
    return answer