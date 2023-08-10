import math
def solution(s):
    answer = 0
    if len(s) == 1 or s == s[::-1]:
        return len(s)
    
    def palindrome(l, r):
        while 0 <= l and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return len(s[l + 1: r])
            
    for i in range(len(s) - 1):
        answer = max(answer,
                     palindrome(i, i),
                     palindrome(i,i+1))
    return answer