n, m = map(int, input().split())

def backtracking(selected, cnt):
    # 현재까지 선택한 숫자의 개수가 m과 같으면 조합 출력
    if cnt == m:
        print(' '.join(map(str, selected)))
        return
    
    # 현재까지 선택한 숫자들 중 가장 큰 숫자보다 큰 숫자들만 선택
    start = selected[-1] + 1 if selected else 1
    for i in range(start, n+1):
        backtracking(selected + [i], cnt + 1)

backtracking([], 0)