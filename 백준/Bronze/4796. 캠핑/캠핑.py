count = 0
while True:
  l, p, v = map(int, input().split())
  count += 1
  if l == 0 and p == 0 and v == 0:
    break
  if v % p > l:
    day = ((v // p) * l) + l
  else:
    day = ((v // p) * l) + (v % p)
  print("Case {}: {}".format(count, day))