def solution(record):
    answer = []
    name = {}
    a = []
    for i in record:
        name[i.split(' ')[-2]] = i.split(' ')[-1]

    for i in record:
        if i.split(' ')[0] == 'Enter':
            answer.append(name[i.split(' ')[-2]]+"님이 들어왔습니다.")
        elif i.split(' ')[0] == 'Leave':
            answer.append(name[i.split(' ')[-1]]+"님이 나갔습니다.")
    return answer