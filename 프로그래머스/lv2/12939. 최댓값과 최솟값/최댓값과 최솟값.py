def solution(s):
    answer = ''
    nums = []
    for i in s.split(' '):
        nums.append(int(i))
    answer += str(min(nums)) + ' ' + str(max(nums))

    return answer
