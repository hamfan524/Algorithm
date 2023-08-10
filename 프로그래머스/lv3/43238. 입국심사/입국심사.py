def solution(n, times):
    answer = 0
    l = 1
    r = n * max(times)
    while l <= r:
        check = 0
        mid = (l + r) // 2
        print(mid)
        for time in times:
            check += mid // time
            if check >= n:
                break
                
        if check >= n:
            answer = mid
            r = mid - 1
        elif check < n:
            l = mid + 1
            
    return answer