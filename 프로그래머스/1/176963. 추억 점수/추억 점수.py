def solution(name, yearning, photo):
    answer = []
    name_dict = dict(zip(name, yearning))
    
    for p in photo:
        total = 0
        for person in p:
            total += name_dict.get(person, 0)
        answer.append(total)
    return answer