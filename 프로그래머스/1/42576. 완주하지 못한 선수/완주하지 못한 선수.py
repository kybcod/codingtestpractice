from collections import Counter

def solution(participant, completion):

    # Counter를 사용하여 각 이름의 개수를 세기
    participant_count = Counter(participant)
    completion_count = Counter(completion)
    #Counter({'mislav': 2, 'stanko': 1, 'ana': 1}) 
    #Counter({'stanko': 1, 'ana': 1, 'mislav': 1})

    # completion 리스트에 없는 이름 찾기
    for name, count in participant_count.items():
        #참가자 명단 수랑 성공 명단 수가 다르면 그 사람 출력
        if count != completion_count[name]:
            answer = name
            break

    return answer