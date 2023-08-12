def solution(N, stages):
    answer, step = [], []
    people = len(stages)
    for i in range(1, N+1):
        if i in stages:
            step.append([i, stages.count(i) / people])
            people -= stages.count(i)
        else:
            step.append([i, 0.0])
    step.sort(key=lambda x: x[1], reverse=True)

    for i in step:
        answer.append(i[0])
    return answer