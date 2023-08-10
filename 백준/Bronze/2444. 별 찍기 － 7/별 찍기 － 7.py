n=int(input())
for i in range(0,n):
    print((" "*(n-(i+1))) + "*"*(2*i+1))
    
for k in range(1,n):
    print((" "*k) + "*"*(2*n-(2*k+1)))