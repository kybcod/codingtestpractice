def solution(name, yearning, photo):
    answer = []
    dic = {}

    for yearn_name, yearn in zip(name, yearning):
        dic[yearn_name] = yearn

    for i in photo:
        sum = 0
        for j in i:
            if j in dic:
                sum += dic[j]
        answer.append(sum)
            
    return answer