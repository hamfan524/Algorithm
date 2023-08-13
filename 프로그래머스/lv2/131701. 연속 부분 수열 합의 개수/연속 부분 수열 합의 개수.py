

def solution(elements):
    answer = set()
    arr = elements * 2

    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.add(sum(arr[j: j + i + 1]))

    return len(answer)