def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)
    for i in range(len(numbers)):
        while True:
            if stack and numbers[stack[-1]] < numbers[i]:
                answer[stack.pop()] = numbers[i]
            else:
                break
        stack.append(i)
    
    return answer