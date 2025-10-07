from itertools import combinations

def solution(relation):
    row_count = len(relation) # 6
    col_count = len(relation[0]) # 4
    candidates = []

    # 1. 모든 열의 조합을 만들어 봄 (1개짜리 ~ 전체)
    for r in range(1, col_count + 1):
        for cols in combinations(range(col_count), r):
            # 2. 현재 조합으로 만든 값들이 중복이 없으면 유일성 O
            seen = set()
            for row in relation:
                key = tuple(row[i] for i in cols)
                seen.add(key)
            if len(seen) == row_count:  # 중복 없으면
                # 3. 최소성 체크 (이미 선택된 후보키의 부분집합이면 안됨)
                is_minimal = True
                for c in candidates:
                    if set(c).issubset(set(cols)):
                        is_minimal = False
                        break
                if is_minimal:
                    candidates.append(cols)

    return len(candidates)
