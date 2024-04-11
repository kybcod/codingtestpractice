def solution(X, Y):
    num = ''
    for i in set(X):
        if i in Y:
            num += i * min(X.count(i), Y.count(i))

    if not num:
        max_num = "-1"
    elif num == '0' * len(num):
        max_num = "0"
    else:
        sorted_num = sorted(num, reverse=True)
        max_num = ''.join(sorted_num)
    return max_num