N, M = list(map(int, input().split()))
#번환해야할 행렬
map_list = [list(map(int, list(input()))) for _ in range(N)]
#목표의 행렬
wanted_list = [list(map(int, list(input()))) for _ in range(N)]

#3x3부분을 다 바꿔주기 위한 함수
def changeAll(start_coord, arr):
    x, y = start_coord
    for i in range(x, x+3):
        for j in range(y, y+3):
            arr[i][j] = 1 - arr[i][j] 

cnt = 0 #횟수 세주는 변수
#행렬을 초과하지 않게 -2만큼 경계준다.
for i in range(0, N-2):
    for j in range(0, M-2):
        #좌표의 값이 같지 않다면
        if map_list[i][j] != wanted_list[i][j]:
            cnt += 1
            changeAll((i,j), map_list)
            
#flag = 0일 때는 변환했다는 것이고, 1일때는 변환해도 동치가 불가
flag = 0
for i in range(N):
    if map_list[i] != wanted_list[i]:
        print(-1)
        flag = 1
        break
if flag == 0:
    print(cnt)