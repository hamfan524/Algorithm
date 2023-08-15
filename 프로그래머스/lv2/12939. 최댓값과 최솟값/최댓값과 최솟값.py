def solution(s):
    answer = ''
    nums = []
    for i in s.split(' '):
        nums.append(int(i))
    return str(min(nums)) + ' ' + str(max(nums))
