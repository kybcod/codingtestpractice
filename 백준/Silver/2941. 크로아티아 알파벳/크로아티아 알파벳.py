string = input()
croatian_alphabets = ["c=","c-","dz=","d-","lj","nj","s=","z="]
cnt = 0
i = 0

while len(string) > i:
    if string[i:i+2] in croatian_alphabets:
        cnt += 1
        i += 2
    elif string[i:i+3] in croatian_alphabets:
        cnt += 1
        i += 3
    else:
        cnt += 1
        i += 1
        
print(cnt)