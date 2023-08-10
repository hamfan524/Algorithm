from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    n = int(input())
    numbers = deque(input()[1:-1].split(','))
    flag = 0

    if n == 0:
        numbers = []
    for i in p:
        if i == "R":
            flag += 1
        elif i == "D":
            if len(numbers) == 0:
                print("error")
                break
            if flag % 2 == 1:
                numbers.pop()
            else:
                numbers.popleft()
    else:
        if flag % 2 == 1:
            numbers.reverse()
        print('[' + ','.join(numbers) + ']')