def binary(l, nList, low, high):
    if low > high:
        return 0
    mid = (low+high)//2
    if l == nList[mid]:
        return 1
    elif l < nList[mid]:
        return binary(l, nList, low, mid-1)
    else:
        return binary(l, nList, mid+1, high)

n = int(input())
A = sorted(map(int, input().split()))
m = input()
M = map(int, input().split())

for l in M:
    low = 0
    high = len(A)-1
    print(binary(l, A, low, high))