def solution(m, musicinfos):
    answer = []
    m = m.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('A#', 'a').replace('G#', 'g')
    for info in musicinfos:
        start, end, name, music = info.split(',')
        h, mm = start.split(':')
        sTime = int(h) * 60 + int(mm)
        h, mm = end.split(':')
        eTime = int(h) * 60 + int(mm)
        playTime = eTime - sTime
        tmp = ''
        i = 0
        music = music.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('A#', 'a').replace('G#', 'g')
        for _ in range(playTime):
            tmp += music[i]
            i = (i + 1) % len(music)

        if m in tmp:
            answer.append([name, playTime])
    
    answer.sort(key= lambda x:x[1], reverse=True)

    return answer[0][0] if answer else "(None)"