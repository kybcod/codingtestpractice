from fractions import Fraction

def solution(N, stages):

    fail = []  # 실패율 저장 리스트

    # 각 스테이지별 실패율 계산
    for i in range(1, N+1):
        challengers = len([x for x in stages if x >= i])  # 해당 스테이지 이상 도달한 사용자 수
        failures = stages.count(i)  # 해당 스테이지에서 멈춰 있는 사용자 수

        if challengers == 0:  # 도달한 플레이어가 없으면 실패율 0
            fail.append((i, Fraction(0)))  # (스테이지 번호, 실패율)
        else:
            fail.append((i, Fraction(failures, challengers)))  # (스테이지 번호, 실패율)

    # 실패율 기준 내림차순 정렬 (실패율이 같으면 스테이지 번호 오름차순)
    fail.sort(key=lambda x: x[1], reverse=True)

    # 정렬된 스테이지 번호 리스트 출력
    sorted_stages = [stage[0] for stage in fail]
    return(sorted_stages) 
