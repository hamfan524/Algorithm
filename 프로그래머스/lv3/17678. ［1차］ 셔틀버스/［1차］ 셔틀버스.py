def solution(n, t, m, timetable):
    lastTime = 540 + (n-1)*t
    waitTime = []
    for table in timetable:
        hour,minute = table.split(":")
        waitTime.append(int(hour)*60 + int(minute))
    waitTime.sort()

    for i in range(n):
        if len(waitTime) < m:
            return "%02d:%02d"%(lastTime//60, lastTime%60)
        if i == n-1:
            if waitTime[0] <= lastTime:
                print(waitTime)
                lastTime = waitTime[m-1] - 1
            return "%02d:%02d"%(lastTime//60, lastTime%60)
        for j in range(m-1, -1, -1):
            busTime = 540 + (i * t)
            if waitTime[j] <= busTime:
                del waitTime[j]
    