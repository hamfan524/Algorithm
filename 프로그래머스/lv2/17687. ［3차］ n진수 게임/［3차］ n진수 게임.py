def solution(n, t, m, p):
    dic = {
        0 : '0',
        1 : '1',
        2 : '2',
        3 : '3',
        4 : '4',
        5 : '5',
        6 : '6',
        7 : '7',
        8 : '8',
        9 : '9',
        10 : 'A',
        11 : 'B',
        12 : 'C',
        13 : 'D',
        14 : 'E',
        15 : 'F'
    }
    nums = ['0']
    for i in range(1, (t*m)+1):
        tmp = ''
        while i > 0:
            tmp = dic[i % n] + tmp  
            i //= n
        nums.append(tmp)
    return ''.join(nums)[p-1:(t*m):m]