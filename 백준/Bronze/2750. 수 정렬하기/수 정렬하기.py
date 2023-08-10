n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(input()))

for i in range(n):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            change = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = change
    print(numbers[i])