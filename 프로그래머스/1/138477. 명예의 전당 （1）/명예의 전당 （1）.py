def solution(k, score):
    answer = []
    winner = []

    for i in score:
        if k > len(winner):
            winner.append(i)
        else:
            if i > min(winner): 
                winner.remove(min(winner))
                winner.append(i)        
        answer.append(min(winner))
    return answer