def solution(N, stages):
    answer = []
    length = len(stages)  # 전체 스테이지 도달자 수 (즉, 총 사용자 수)
    
    # 1번부터 N번 스테이지까지 반복
    for i in range(1, N+1):
        cnt = stages.count(i)  # 현재 스테이지 i에 머물러 있는 사람 수 (즉, 실패한 사람 수)
        
        if length == 0:  # 만약 지금까지 남은 사람이 없으면 실패율 0
            failure_rate = 0
        else:
            failure_rate = cnt / length  # 실패율 = 해당 스테이지 실패자 수 / 그 스테이지에 도달한 사람 수
        
        answer.append((i, failure_rate))  # 스테이지 번호와 실패율을 튜플로 리스트에 추가
        length -= cnt  # 다음 스테이지 도달자 수 = 현재 남은 사람 수 - 현재 스테이지에서 실패한 사람 수
    
    # 실패율 기준으로 내림차순 정렬
    answer = sorted(answer, key=lambda x: x[1], reverse=True)
    
    # 스테이지 번호만 추출해서 반환
    answer = [i[0] for i in answer]
    
    return answer
