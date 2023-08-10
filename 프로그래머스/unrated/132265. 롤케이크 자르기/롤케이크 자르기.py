def solution(topping):
    answer = 0
    left = set()
    right = set()
    leftDp = [0] * len(topping)
    rightDp = [0] * len(topping)
    
    for i in range(len(topping)):
        left.add(topping[i])
        leftDp[i] = len(left)
        right.add(topping[len(topping) - (i + 1)])
        rightDp[len(topping) - (i + 1)] = len(right)

    for i in range(len(topping)-1):
        if leftDp[i] == rightDp[i+1]:
            answer += 1

    return answer