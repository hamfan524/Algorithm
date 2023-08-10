def solution(storey):
    answer = 0
    while storey: 
        if storey % 10 == 5 and (storey // 10) % 10 >= 5:
            answer += 10 - (storey % 10)
            storey = (storey // 10) + 1

        elif storey % 10 > 5:
            answer += 10 - (storey % 10)
            storey = (storey // 10) + 1
        else:
            answer += storey % 10
            storey //= 10

    return answer
