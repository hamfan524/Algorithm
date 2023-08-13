from itertools import combinations
import math

def solution(nums):
    answer = 0
    bools = True
    comb = list(combinations(nums, 3))
    arr = []
    
    for i in comb:
        arr.append(sum(i))
    
    for i in arr:
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                bools = False
        if bools == True:
            answer += 1
        bools = True
    return answer