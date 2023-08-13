def solution(n, k):
    answer = 0
    num = ''
    while n > k:
        num += str(n % k)
        n //= k
    num += str(n)
    nums = num[::-1].split('0')
    for i in nums:
        isPrime = True
        if not i or i == '1':
            continue
        for j in range(2, int(int(i)**0.5) + 1):
            if int(i) % j == 0:
                isPrime = False
                break
        if isPrime:
            answer += 1
            isPrime = False 
    return answer