def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    union = []
    st1 = []
    intersection = []
    for i in range(len(str1)-1):
        if 97 <= ord(str1[i]) <= 122 and 97 <= ord(str1[i+1]) <= 122:
            st1.append(str1[i:i+2])
            union.append(str1[i:i+2])
    for j in range(len(str2)-1):
        if 97 <= ord(str2[j]) <= 122 and 97 <= ord(str2[j+1]) <= 122:
            if str2[j:j+2] in st1:
                st1.remove(str2[j:j+2])
                intersection.append(str2[j:j+2])
            else:
                union.append(str2[j:j+2])
            
    return int(len(intersection) / len(union) * 65536) if len(union) != 0 else 65536