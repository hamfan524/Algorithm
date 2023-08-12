dic = {
    'E' : (0, 1),
    'S' : (1, 0),
    'W' : (0, -1),
    'N' : (-1, 0)
}
def start(x, y, park, routes):
    global dic
    check = True
    tmp = [(x, y)]
    for i in routes:
        a, b = tmp.pop()
        xx, yy = dic[i[0]]
        nx, ny = a, b
        for _ in range(int(i[-1])):
            nx += xx
            ny += yy
            if nx in range(len(park)) and ny in range(len(park[0])) and park[nx][ny] != "X":
                tmp.append((nx, ny))
            else:
                check = False
                
        if check == False:
            tmp.pop()
            tmp.append((a, b))
            check = True    
    return tmp[-1]
    
def solution(park, routes):
    for i in range(len(park)):
        for j in range(len(park[i])):
            if park[i][j] == 'S':
                answer = start(i, j, park, routes)
                
    return answer

