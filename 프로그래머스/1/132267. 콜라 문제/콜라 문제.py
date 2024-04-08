def solution(a, b, n):
    answer = 0
    while n >= a:
        # new : 콜라 빈 병의 개수를 가져다주면서 얻을 수 있는 새로운 콜라의 개수
        new = (n // a) * b
        left = n % a
        answer += new 
        n = new + left
    return answer