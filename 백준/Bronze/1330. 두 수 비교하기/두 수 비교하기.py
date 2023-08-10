A = list(map(int, input().split()))

if A[0] > A[1]:
  print(">")
elif A[1] > A[0]:
  print("<")
else:
  print("==")
