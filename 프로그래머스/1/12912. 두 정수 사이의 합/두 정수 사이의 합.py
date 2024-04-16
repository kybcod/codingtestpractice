def solution(a, b):
    answer = 0
    ma = min(a,b)
    mb = max(a,b)
    for i in range(ma,mb+1):
        answer += i
    return answer