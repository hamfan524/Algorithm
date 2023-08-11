dic = []
words = 'AEIOU'

def dfs(depth, tmp):
    global dic
    global words
    
    if depth == 5:
        return
    
    for i in range(5):
        dic.append(tmp + words[i])
        dfs(depth+1, tmp + words[i])
        
def solution(word):
    global dic
    dfs(0, "")
    return sorted(dic).index(word) + 1