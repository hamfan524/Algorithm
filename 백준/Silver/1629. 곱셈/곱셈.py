def pow(a, b, c):
    if b == 0:
        return 1 % c
    elif b == 1:
        return a % c
    elif b % 2 == 0:
        tmp = pow(a, b // 2, c)
        return (tmp * tmp) % c
    else:
        tmp = pow(a, (b - 1) // 2, c)
        return (tmp * tmp * a) % c

a, b, c = map(int, input().split())
print(pow(a, b, c))