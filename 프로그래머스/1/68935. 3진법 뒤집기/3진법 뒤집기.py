def solution(n):
    # 1. 10진수를 3진법 문자열로 변환
    ternary = ""
    while n > 0:
        n, remainder = divmod(n, 3)
        ternary = str(remainder) + ternary

    reversed_ternary = ternary[::-1]
    return int(reversed_ternary, 3)
