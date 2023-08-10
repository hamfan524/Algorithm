n = int(input())

mod = 1000000
a, b = 0, 1

n = n % (15 * mod)
for i in range(n):
    a, b = b % mod, (a+b) % mod

print(a)