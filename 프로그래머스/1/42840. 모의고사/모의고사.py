def solution(answers):
    result = []

    person1 = [1, 2, 3, 4, 5] 
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0,0,0]

    # score 배열에 학생들 성적 넣기
    for index, answer in enumerate(answers):
        if answer == person1[index % len(person1)]:
            score[0] += 1
        if answer == person2[index % len(person2)]:
            score[1] += 1
        if answer == person3[index % len(person3)]:
            score[2] += 1

    for i,s in enumerate(score):
        if s == max(score):
            result.append(i+1)
            
    return result