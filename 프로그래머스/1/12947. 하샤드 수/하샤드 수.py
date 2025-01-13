def solution(x):
    n = [int(i) for i in str(x)]
    n = sum(n)
    if x % n == 0:
        return (True)
    else:
        return (False)