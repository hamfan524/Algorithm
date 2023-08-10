sum_list = []

while True:
  a, b = list(map(int, input().split()))
  sum_list.append(a + b)
  if a == 0 and b == 0:
    break

i = 0
while sum_list[i] != 0:
  print(sum_list[i])
  i += 1
