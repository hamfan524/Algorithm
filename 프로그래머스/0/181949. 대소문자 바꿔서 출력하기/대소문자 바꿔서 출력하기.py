str = input()
result = ""
for s in str:
    if ord(s) >= 92:
        result += chr(ord(s) - 32)
    else:
        result += chr(ord(s) + 32)
        
print(result)