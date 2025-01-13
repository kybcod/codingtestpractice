def solution(n):
    cnt = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1
        cnt += 1

        if cnt > 500:  # 500번 초과 시 -1 반환
            return -1

    return cnt  # n이 1이 되면 반복 횟수 반환