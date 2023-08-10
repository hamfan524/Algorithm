def solve(n, brands):
    brands.sort()
    totalPrice = brands[0][0]
    brands.sort(key = lambda x : x[1])
    singlePrice = brands[0][1]
    
    if singlePrice * 6 < totalPrice:
        return n * singlePrice
    
    if n % 6 == 0:
        return totalPrice * (n // 6)
    else:
        return totalPrice * (n // 6) + min(totalPrice, singlePrice * (n % 6))

N, M = map(int, input().split())
brands = [list(map(int, input().split())) for _ in range(M)]

print(solve(N, brands))