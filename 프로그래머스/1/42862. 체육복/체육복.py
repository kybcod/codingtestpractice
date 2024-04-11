def solution(n, lost, reserve):
    total = [1] * n

    for i in lost:
        total[i-1] -= 1

    for j in reserve:
        total[j-1] += 1

    # 체육복 빌려주기
    for idx, num in enumerate(total):
        # 체육복이 없는 학생인 경우
        if num == 0:

            # 앞 번호 학생이 여벌의 체육복을 가지고 있는지 확인
            if idx > 0 and total[idx - 1] == 2:
                total[idx] = 1
                total[idx - 1] = 1

            # 뒷 번호 학생이 여벌의 체육복을 가지고 있는지 확인
            elif idx < n - 1 and total[idx + 1] == 2:
                total[idx] = 1
                total[idx + 1] = 1

    # 수업을 들을 수 있는 학생 수 계산
    answer = sum(1 for x in total if x > 0)
    return answer