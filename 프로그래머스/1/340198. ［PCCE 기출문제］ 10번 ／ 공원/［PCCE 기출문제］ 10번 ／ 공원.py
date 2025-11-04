def solution(mats, park):
    mats.sort(reverse=True)  # 1️⃣ 큰 돗자리부터 시도
    n, m = len(park), len(park[0])  # 2️⃣ park의 행, 열 길이 저장

    for size in mats:  # 3️⃣ 각 돗자리 크기를 하나씩 확인
        for i in range(n - size + 1):  # 4️⃣ 세로로 놓을 수 있는 시작점들
            for j in range(m - size + 1):  # 5️⃣ 가로로 놓을 수 있는 시작점들
                can_place = True  # 6️⃣ 현재 위치에 깔 수 있다고 가정하고 시작

                # 7️⃣ (i, j)를 왼쪽 위로 하는 size×size 구역 확인
                for x in range(i, i + size):
                    for y in range(j, j + size):
                        if park[x][y] != "-1":  # 사람이 있거나 자리 차지됨
                            can_place = False  # 깔 수 없음
                            break  # 이 행 중단
                    if not can_place:
                        break  # 이 정사각형 중단

                # 8️⃣ size×size 구역이 모두 비어있다면
                if can_place:
                    return size  # 바로 그 크기 반환 (큰 돗자리부터 탐색 중이므로)

    # 9️⃣ 모든 돗자리를 시도해도 못 깔았으면
    return -1
