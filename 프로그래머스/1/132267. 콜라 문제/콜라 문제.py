def solution(a, b, n):
    answer = 0
    while n >= a:
        new = (n // a) * b
        left = n % a
        answer += new 
        n = new + left
    return answer