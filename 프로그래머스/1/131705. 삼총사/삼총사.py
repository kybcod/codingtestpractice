from itertools import combinations
def solution(number):
    count = 0
    # 3명을 선택하는 모든 조합을 생성
    for comb in combinations(number, 3):
        if sum(comb) == 0:  # 합이 0인지 확인
            count += 1
    return count