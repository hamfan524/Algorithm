n = int(input())
a = list(map(int, input().split()))

a.sort()

answer = 1

for i in a: 
  if answer < i:
    break
  answer += i

print(answer)  
