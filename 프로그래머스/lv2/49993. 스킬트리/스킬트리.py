def solution(skill, skill_trees):
    answer = 0
    
    for s in skill_trees:
        check = True
        i = 0
        j = 0
        print(s) 
        while i < len(s):
            print(s[i])
            if s[i] not in skill:
                i += 1
            else:
                if s[i] != skill[j]:
                    check = False
                    break
                else:
                    i += 1
                    j += 1
                    
        if check == False:
            check = True
            answer += 1

    return len(skill_trees) - answer