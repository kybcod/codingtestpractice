def solution(survey, choices):
    answer = ''
    types = {"R":0, "T":0, "C":0, "F":0, "J":0, "M":0, "A":0, "N":0}
    
    for i in range(len(survey)):
        first, second = survey[i][0], survey[i][1]
        choice = choices[i]
        
        if choice < 4:  # 비동의 쪽
            types[first] += 4 - choice
        elif choice > 4:  # 동의 쪽
            types[second] += choice - 4
    
    pairs = [("R", "T"), ("C", "F"), ("J", "M"), ("A", "N")]
    for a, b in pairs:
        if types[a] >= types[b]:
            answer += a
        else:
            answer += b
            
    return answer
