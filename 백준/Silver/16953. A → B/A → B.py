def changeNum(a, b):
    cnt = 0
    while b > a:
        if b % 10 == 1:
            b = b // 10
            cnt += 1
        elif b % 2 == 0:
            b //= 2
            cnt += 1
        else:
            break
    if a == b:
        return cnt + 1
    else:
        return -1

A, B = map(int, input().split())

print(changeNum(A, B))