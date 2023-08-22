def solution(files):
    answer = []
    for f in files:
        head, number, tail = '', '', ''
        headPass = False
        for i in range(len(f)):
            if f[i].isdigit():
                number += f[i]
                headPass = True
            elif headPass == False:
                head += f[i]
            else:
                tail += f[i:]
                break
        answer.append((head, number, tail))
        
    answer.sort(key= lambda x: (x[0].lower(), int(x[1])))    
            
    return [''.join(t) for t in answer]