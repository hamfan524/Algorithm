from collections import Counter
def solution(want, number, discount):
    answer = 0
    fruits = {}
    for i in range(len(want)):
        fruits[want[i]] = number[i]
    for i in range(len(discount) - 9):
        check = Counter(discount[i: i+10])
        if fruits == check:
            answer += 1
    return answer