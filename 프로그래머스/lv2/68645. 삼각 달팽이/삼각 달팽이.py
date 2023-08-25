direction = ((1, 0), (0, 1), (-1, -1))

def solution(n):
    snail = [[0] * i for i in range(1, n + 1)]
    x, y, num = -1, 0, 1
    for i in range(n):
        for _ in range(i, n):
            dx, dy = direction[i % 3]
            x, y = x + dx, y + dy
            snail[x][y] = num
            num += 1

    return sum(snail, [])
