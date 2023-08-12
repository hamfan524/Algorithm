def solution(today, terms, privacies):
    answer = []
    term_dic = {}
    tYear, tMonth, tDate = today.split('.')
    todayDate = (int(tYear)*12*28) + (int(tMonth)*28) + int(tDate)

    for i in terms:
        a, b = i.split(' ')
        term_dic[a] = int(b)
    for i in range(len(privacies)):
        day, term = privacies[i].split(' ')
        year, month, date = day.split('.')
        termDate = (int(year)*12*28) + (int(month)*28) + int(date)
        
        if term_dic[term] * 28 <= todayDate - termDate:
            answer.append(i + 1)
    return answer