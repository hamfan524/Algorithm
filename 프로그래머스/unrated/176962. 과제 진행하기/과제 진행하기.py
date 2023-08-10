def solution(plans):
    answer = []
    stopSub = []
    plans.sort(key = lambda x: x[1])
    
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        h, m = start.split(':')
        time = int(h) * 60 + int(m)
        plans[i] = [name, time, int(playtime)]
    
    time = 0
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        
        while stopSub:
            _name, _playtime = stopSub.pop()
            if time >= _playtime:
                time -= _playtime
                answer.append(_name)
            else:
                stopSub.append((_name, _playtime - time))
                break
        stopSub.append((name, playtime))
        
        if i < len(plans) - 1:
            ns = plans[i+1][1]
            time = ns - start
    
    while stopSub:
        _name, _ = stopSub.pop()
        answer.append(_name)
        
    return answer
