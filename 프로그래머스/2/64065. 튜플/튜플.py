def solution(s):
    answer = []
    
    s = s[2:-2]
    parts = s.split('},{')
    sets =[list(map(int, part.split(','))) for part in parts]
    sets.sort(key=len)
    
    for strr in sets:
        for i in strr:
            if i not in answer:
                answer.append(i)
    return answer