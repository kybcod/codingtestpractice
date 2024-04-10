def solution(N, stages):
    answer = []
    length = len(stages) # 전체 스테이지 도달자 수
    for i in range(1, N+1):
        cnt = stages.count(i) #유저 수
        if length == 0:
            failure_rate = 0 # 실패율 0
        else: #유저수/전체도달자수
            failure_rate = cnt / length
        answer.append((i, failure_rate)) # (i, failure_rate) 튜플이 리스트에 추가
        length -= cnt #이전 스테이지 도달자 수 - 현재 스테이지에 머무르고 있는 유저의 수 c
    answer = sorted(answer, key=lambda x: x[1], reverse= True) # 실패율 기준으로 내림차순
    answer = [i[0] for i in answer]
    return answer