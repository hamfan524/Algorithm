from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    user = defaultdict(set)
    cnt = defaultdict(int)

    for r in list(set(report)):
        a, b = r.split()
        user[a].add(b)
        cnt[b] += 1

    for i in id_list:
        result = 0
        for u in user[i]:
            if cnt[u] >= k:
                result += 1
        answer.append(result)
    
    return answer