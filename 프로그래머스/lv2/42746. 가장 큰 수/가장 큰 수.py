def solution(numbers):
    answer = ''
    num = []
    for i in numbers:
        num.append(str(i))
    num.sort(key=lambda i: i*3, reverse=True)
    for i in num:
        answer += i
    answer = int(answer)
    return str(answer)