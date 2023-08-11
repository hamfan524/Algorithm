def solution(dirs):
    dp = set()

    dic = {
        'U' : [-1, 0],
        'D' : [1, 0],
        'R' : [0, 1],
        'L' : [0, -1]
    }
    graph = [[0] * 11 for _ in range(11)]

    dx, dy = 5, 5
    for i in dirs:
        x, y = dic[i]
        nx = dx - x
        ny = dy - y
        if 0 <= nx < 11 and 0 <= ny < 11:
            dp.add(((dx, dy), (nx, ny)))
            dp.add(((nx,ny), (dx, dy)))
            dx, dy = nx, ny

    return len(dp) // 2