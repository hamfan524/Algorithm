def solution(numbers):
    answer = []
    for num in numbers:
        pNum = ((num ^ (num+1)) >> 2) + 1
        answer.append(num + pNum)
    return answer