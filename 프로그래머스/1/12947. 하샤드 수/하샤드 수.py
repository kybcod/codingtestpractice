def solution(x):
    sum_ch = sum(int(i) for i in str(x))
    answer = True
    return True if x % sum_ch == 0 else False