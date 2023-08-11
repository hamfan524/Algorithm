from collections import deque

def solution(prices):
    prices = deque(prices)
    answer = []
    while prices:
        time = 0
        price = prices.popleft()
        for i in prices:
            time += 1
            if price > i: 
                break
        answer.append(time)

    return answer