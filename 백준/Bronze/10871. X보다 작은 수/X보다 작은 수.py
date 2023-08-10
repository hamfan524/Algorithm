n, x = map(int, (input().split()))
a = list(map(int, (input().split())))

b = [a[i] for i in range(n) if a[i] < x]
for j in b:
   print(j, end=" ")