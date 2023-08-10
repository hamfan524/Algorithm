a = 0
b = str(input())
for i in b:
    print(i,end='')
    a = a + 1
    if a == 10:
        print()
        a = 0