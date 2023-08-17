from math import ceil
def solution(fees, records):
    answer = []
    stdTime, stdFee, t, money = fees[0], fees[1], fees[2], fees[3]
    park = {}
    tmp = {}

    for r in records:
        time, number, state = r.split(' ')
        h, m = time.split(':')
        recordTime = int(h) * 60 + int(m)
        if state == "IN":
            park[number] = recordTime
        else:
            useTime = recordTime - park.pop(number)
            if number not in tmp:
                tmp[number] = useTime
            else:
                tmp[number] += useTime
    if park:
        for p in park:
            if p not in tmp:
                tmp[p] = (1439 - park[p])
            else:
                tmp[p] += (1439 - park[p])
    for r in sorted(tmp.keys()):
        if tmp[r] - stdTime <= 0:
            answer.append(stdFee)
        else:       
            answer.append(ceil((tmp[r] - stdTime) / t) * money + stdFee)

    return answer