def solution(n):
    a = str(n);
    sum = 0
    for i in range(len(a)):
        sum += int(a[i])
    return sum