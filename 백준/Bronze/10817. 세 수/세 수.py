a,b,c = map(int,input().split())
if a>=b>=c:
    print(b)    
elif a<=b<=c:
    print(b)
elif c>=a>=b:
    print(a)
elif c<=a<=b:
    print(a)
elif a<=c<=b:
    print(c)
elif a>=c>=b:
    print(c)