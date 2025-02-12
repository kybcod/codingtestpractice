def solution(babbling):
    answer = 0
    li = ["aya", "ye", "woo", "ma"]
    
    for b in babbling:
        for l in li:
            if l * 2 not in b:
                b = b.replace(l, ' ')
        
        if b.isspace():
            answer += 1
    return answer