def solution(d, budget):
    cnt = 0
    sum = 0

    for i in sorted(d):
        sum += i
        if sum <= budget:
            cnt += 1
    return cnt