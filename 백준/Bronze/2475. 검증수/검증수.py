number = list(map(int, input().split()))
result = 0
for i in number:
    result += (i * i)

print(result % 10)