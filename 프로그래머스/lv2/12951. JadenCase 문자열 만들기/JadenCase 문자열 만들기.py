def solution(s):
    answer = []
    for st in s.split(' '):
        st = list(st)
        for i in range(len(st)):
            if st[i].isdigit():
                continue
            if i == 0:
                st[i] = st[i].upper()
            else:
                st[i] = st[i].lower()
        answer.append(''.join(st))

    return ' '.join(answer)
                      